import json
import re
import pathlib
import glob
import os
import csv
import uuid

import biothings_client
import requests


def get_taxon_info(_ids):
    """retrieve ncbi taxonomy information from biothings_client
    taxonomy information includes "scientific_name", "parent_taxid", "lineage", and "rank"

    :param _ids: a set of ncbi taxon ids obtained from Disbiome Experiment database "organism_ncbi_id"
    :return: a dictionary with query _ids (taxids) as the keys and taxonomy fields with the query _id as values
    """
    _ids = set(_ids)
    t = biothings_client.get_client("taxon")
    taxon_info = t.gettaxa(
        _ids, fields=["scientific_name", "parent_taxid", "lineage", "rank"]
    )
    taxon_info = {
        t["query"]: t for t in taxon_info if "notfound" not in t.keys()
    }
    yield taxon_info


def get_mondo_doid_id(meddra_ids):
    """retrieve mapped mondo or disease ontology id with meddra_id

    :param meddra_ids: a set of meddra_ids (diseases) obtained from Disbiome Experiment database "meddra_id"
    :return: a dictionary with mondo_id or disease ontology id as the keys and meddra_ids as the values
    """
    meddra_ids = set(meddra_ids)
    d = biothings_client.get_client("disease")
    query_op = d.querymany(
        meddra_ids,
        scopes=["mondo.xrefs.meddra", "disease_ontology.xrefs.meddra"],
        fields=["mondo.xrefs.meddra", "disease_ontology.doid"],
    )
    query_op = {
        d["query"]: d.get("_id")
        for d in query_op
        if "notfound" not in query_op
    }
    yield query_op


def meddra_id_mapping(path, meddra_ids):
    mapped = []
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader, None)
        for data in reader:
            meddra_id = data[0].split(":")[1]
            if meddra_id in meddra_ids:
                mapped.append({data[0]: data[2]})
    # print(f"Total mapped meddra_ids: {len(mapped)}", mapped)
    yield mapped


def get_mapping_info():
    path = os.path.join(pathlib.Path.cwd(), "mappings/")
    assert path
    files = glob.glob(f"{path}*.tsv")
    yield files


def combine_meddra_mappings(meddra_ids):
    files = get_mapping_info()
    combined_mappings = []
    for obj in files:
        for mapping_dict in obj:
            mappings = meddra_id_mapping(mapping_dict, meddra_ids)
            for mapping in mappings:
                combined_mappings.extend(mapping)
    yield combined_mappings


def update_subject_node(subject_node, bt_taxon):
    """update the subject_node dictionary with the info from biothings_client taxon info
    old keys: "organism_ncbi_id", "organism_name"
    new keys: "scientific_name", "parent_taxid", "lineage", "rank"

    :param subject_node: a dictionary with ncbi organism taxon info from Disbiome Experiment database
    :param bt_taxon: a dictionary with ncbi organism taxon info retrieved from biothings_client
    :return: an updated dictionary with info from both Disbiome and biothings_client
    """
    if subject_node["id"] in bt_taxon:
        taxon_info = bt_taxon[subject_node["id"]]
        new_taxon_keys = ["scientific_name", "parent_taxid", "lineage", "rank"]
        for key in new_taxon_keys:
            subject_node[key] = taxon_info.get(key)


def get_publication():
    """retrieve publication relevant information regarding the Disbiome experiment data
    from https://disbiome.ugent.be:8080/publication

    :return: a dictionary with info retrieved from Disbiome publication database
    :return keys: "publication_id", "title", "pubmed_url", and "pmcid" or "pmid"
    """
    pub_url = "https://disbiome.ugent.be:8080/publication"
    pub_resp = requests.get(pub_url)
    pub_content = json.loads(pub_resp.content)
    pub_all = {}
    for pub in pub_content:
        pubmed_url = pub.get("pubmed_url")
        doi = pub.get("doi")

        pub_dict = {
            "publication_id": pub["publication_id"],
            "title": pub["title"],
        }
        pub_all.update({pub_dict["publication_id"]: pub_dict})

        if pubmed_url:
            pub_dict = {
                "publication_id": pub["publication_id"],
                "title": pub["title"]
            }
            pub_all.update({pub_dict["publication_id"]: pub_dict})
            # some pubmed_url have pmid and some have pmcid in it, some don't follow those rules at all
            # "pubmed_url": "https://www.ncbi.nlm.nih.gov/pubmed/25446201"
            # "pubmed_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4646740/"
            pmid_match = re.match(r".*?\/(\d+)", pubmed_url)
            pmcid_match = re.match(r".*?(PMC)(\d+)", pubmed_url)
            if pmcid_match:
                pub_dict["pmcid"] = pmcid_match.groups()[1]
                pub_all.update({pub_dict["publication_id"]: pub_dict})
            elif pmid_match:
                pub_dict["pmid"] = pmid_match.groups()[0]
                pub_all.update({pub_dict["publication_id"]: pub_dict})
            else:
                pub_dict["pubmed_url"] = pub["pubmed_url"]
                pub_all.update({pub_dict["publication_id"]: pub_dict})
        if doi:
            pub_dict["doi"] = pub["doi"]
            pub_all.update({pub_dict["publication_id"]: pub_dict})

    yield pub_all


def get_association(content_dict, keys):
    """create association dictionary with different key contents
    some json objects from Disbiome do not have "sample_name", "host_type", or "control_name"

    :param content_dict: a json object retrieved from https://disbiome.ugent.be:8080/experiment
    :param keys: a list of "sample_name", "host_type", "control_name" will be used as dictionary keys
    :return: an association dictionary with different key contents
    """
    association = {
        "predicate": "OrganismalEntityAsAModelOfDiseaseAssociation",
        "qualifier": content_dict["qualitative_outcome"].lower()
    }

    for key in keys:
        if content_dict[key]:
            association[key] = content_dict[key].lower()
    return association


def load_disbiome_data():
    """load data from Disbiome Experiment database
    10837 records originally in Disbiome Experiment data
    10742 records have ncbi_taxid and 95 records do not
    8420 records without duplicated out_put dictionary _id
    ncbi_taxid: 1535 without duplicates
    meddra_id: 322 without duplicates, 46 meddra_id are mapped to MONDO (276 has no mapping)

    :return: an iterator of dictionary composed of subject_node, object_node, association_node, and publication_node
    """
    # The experimental and publication data from Disbiome is on a static webpage
    exp_url = "https://disbiome.ugent.be:8080/experiment"

    exp_resp = requests.get(exp_url)
    exp_content = json.loads(exp_resp.content)

    # by_taxon is a generator object, so can be only used once
    bt_taxon = get_taxon_info(
        js["organism_ncbi_id"] for js in exp_content if js["organism_ncbi_id"]
    )
    # convert the generator object to a list
    taxons = list(bt_taxon)

    bt_disease = get_mondo_doid_id(
        js["meddra_id"] for js in exp_content if js["meddra_id"]
    )

    # remove the None mondo dictionary values
    bt_disease = {
        meddra: mondo
        for disease_obj in bt_disease
        for meddra, mondo in disease_obj.items()
        if mondo
    }

    meddra_ids = set([str(js["meddra_id"]) for js in exp_content])
    mapping_info = combine_meddra_mappings(meddra_ids)
    meddra_mappings = {k.split(":")[1]: mapping for obj_l in mapping_info for mapping in obj_l for k, v in mapping.items()}

    # get publication information
    pub_data = get_publication()
    publications = list(pub_data)

    for js in exp_content:
        if js["organism_ncbi_id"]:
            subject_node = {
                "id": f"taxid:{str(js['organism_ncbi_id'])}",
                "organism_name": js["organism_name"].lower(),
                "type": "biolink:OrganismalEntity"
            }
            for taxon in taxons:
                update_subject_node(subject_node, taxon)

        else:
            subject_node = {
                "organism_name": js["organism_name"].lower(),
                "type": "biolink:OrganismalEntity"
            }

        object_node = {
            "name": js["disease_name"].lower(),
            "type": "biolink:Disease"
        }

        if js["meddra_id"]:
            object_node.update({
                "id": None,
                "meddra_id": str(js["meddra_id"]),
                "meddra_level": js["meddra_level"],
            })

            if object_node["meddra_id"] in bt_disease:
                mondo_id = bt_disease[object_node["meddra_id"]]
                object_node["id"] = mondo_id
                object_node["mondo"] = mondo_id.split(":")[1]
            elif object_node["meddra_id"] in meddra_mappings:
                # dict ex. {'10002026': {'MedDRA:10002026': 'EFO:0000253'}}
                key = f"MedDRA:{object_node['meddra_id']}"
                # return 'EFO' from 'EFO:0000253'
                id_key = meddra_mappings[object_node["meddra_id"]][key].split(":")[0]
                # return 'EFO:0000253'
                object_node["id"] = meddra_mappings[object_node["meddra_id"]][key]
                # return '0000253' from 'EFO:0000253'
                object_node[id_key] = meddra_mappings[object_node["meddra_id"]][key].split(":")[1]
            else:
                object_node["id"] = f"meddra:{object_node['meddra_id']}"

            js_keys = ["sample_name", "method_name", "host_type", "control_name"]
            association = get_association(js, js_keys)

            # n1 = subject_node["organism_name"].split(" ")[0]
            # n2 = object_node["name"].replace(" ", "_")
            for pub in publications:
                output_dict = {
                    "_id": uuid.uuid4(),
                    # "edge": f"{n1}_associated_with_{n2}",
                    "association": association,
                    "object": object_node,
                    "subject": subject_node,
                    "publications": pub[js["publication_id"]],
                }
                yield output_dict


for data in load_disbiome_data():
    print(data)
