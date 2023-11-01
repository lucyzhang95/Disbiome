import json
import re

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
        fields="mondo.xrefs.meddra",
    )
    query_op = {
        d["query"]: d.get("_id")
        for d in query_op
        if "notfound" not in query_op
    }
    yield query_op


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
        if pubmed_url is None:
            pub_dict = {
                "publication_id": pub["publication_id"],
                "title": pub["title"],
            }
            pub_all.update({pub_dict["publication_id"]: pub_dict})
            # print(f"No pubmed_url: publication_id: {pub['publication_id']}, {pub['title']}.")
        else:
            # some pubmed_url have pmid and some have pmcid in it, some don't follow those rules at all
            # "pubmed_url": "https://www.ncbi.nlm.nih.gov/pubmed/25446201"
            # "pubmed_url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4646740/"
            pmid_match = re.match(r".*?\/(\d+)", pubmed_url)
            pmcid_match = re.match(r".*?(PMC)(\d+)", pubmed_url)
            pub_dict = {
                "publication_id": pub["publication_id"],
                "title": pub["title"],
            }
            if pmcid_match:
                pub_dict["pubmed_url"] = pub["pubmed_url"]
                pub_dict["pmcid"] = pmcid_match.groups()[1]
                pub_all.update({pub_dict["publication_id"]: pub_dict})
            elif pmid_match:
                pub_dict["pubmed_url"] = pub["pubmed_url"]
                pub_dict["pmid"] = pmid_match.groups()[0]
                pub_all.update({pub_dict["publication_id"]: pub_dict})
            else:
                pub_dict["pubmed_url"] = pub["pubmed_url"]
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
        "qualifier": content_dict["qualitative_outcome"].lower(),
        "method": content_dict["method_name"],
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

    pub_data = get_publication()
    publications = list(pub_data)

    no_taxid = []
    for js in exp_content:
        if js["organism_ncbi_id"]:
            subject_node = {
                "id": str(js["organism_ncbi_id"]),
                "organism_name": js["organism_name"].lower(),
            }

            for taxon in taxons:
                update_subject_node(subject_node, taxon)

            object_node = {
                "meddra_id": str(js["meddra_id"]),
                "name": js["disease_name"].lower(),
                "meddra_level": js["meddra_level"],
            }

            if object_node["meddra_id"] in bt_disease:
                mondo_id = bt_disease[object_node["meddra_id"]].split(":")[1]
                object_node["id"] = mondo_id
                object_node["mondo"] = mondo_id
            else:
                object_node["id"] = object_node["meddra_id"]

            js_keys = ["sample_name", "host_type", "control_name"]
            association = get_association(js, js_keys)

            n1 = subject_node["organism_name"].split(" ")[0]
            n2 = object_node["name"].replace(" ", "_")
            predicate = "OrganismalEntityAsAModelOfDiseaseAssociation"

            for pub in publications:
                output_dict = {
                    "_id": f"{subject_node['id']}_{predicate}_{object_node['id']}",
                    "edge": f"{n1}_associated_with_{n2}",
                    "association": association,
                    "object": object_node,
                    "subject": subject_node,
                    "publications": pub[js["publication_id"]],
                }
                yield output_dict

        else:
            no_taxid.append(
                {
                    "Experiment_id": js["experiment_id"],
                    "organism": js["organism_name"],
                    "disease": js["disease_name"],
                }
            )
    # print(no_taxid)
