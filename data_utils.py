from disbiome_parser import load_disbiome_data
import os
import pickle

import pandas as pd
import biothings_client


class SaveData:
    disbiome_data = None

    def __init__(self):
        self.disbiome_data = load_disbiome_data()

    def save_disbiome_data_to_pkl(self, output_path):
        parser_op = []
        for obj in self.disbiome_data:
            parser_op.append(obj)
        with open(output_path, 'wb') as handle:
            pickle.dump(parser_op, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return parser_op


class DataManipulation:
    def __init__(self, input_path):
        with open(input_path, 'rb') as handle:
            self.disbiome_data = pickle.load(handle)

    def count_node_pair(self, node1, node2, node_str1, node_str2):
        unique_pair = []
        for d in self.disbiome_data:
            if node_str1 in d[node1] and node_str2 in d[node2]:
                pair = f"{d[node1][node_str1]}-{d[node2][node_str2]}"
                unique_pair.append(pair)
        message = f"Number of unique pairs of {node1, node_str1}-{node2, node_str2}: {len(set(unique_pair))}"
        return message

    def map_lineage_taxids(self):
        taxid_lineage = []
        for d in self.disbiome_data:
            if "lineage" in d["subject"]:
                for taxid in d["subject"]["lineage"]:
                    taxid_lineage.append(taxid)

        t = biothings_client.get_client("taxon")
        query = t.gettaxa(set(taxid_lineage), fields=["scientific_name", "rank"])
        # ranks = [d["rank"] for d in query]
        # rank_set = set(ranks)
        lineage_d = {int(t["query"]): t for t in query if "notfound" not in t.keys()}
        return lineage_d

    def get_lineage_rank_data(self, mapped_lineage_taxids):
        lineage_rank_data = []
        for d in self.disbiome_data:
            if "taxid" in d["subject"] and "lineage" in d["subject"] and "parent_taxid" in d["subject"]:
                microbe_d = {
                    "taxid": d["subject"]["taxid"],
                    "lineage": d["subject"]["lineage"],
                    "parent_taxid": d["subject"]["parent_taxid"]
                }
                lineage_rank_data.append(microbe_d)

        for rank_d in lineage_rank_data:
            for taxid in rank_d["lineage"]:
                if taxid in mapped_lineage_taxids:
                    rank_d.update({mapped_lineage_taxids[taxid]["rank"]: (mapped_lineage_taxids[taxid]["scientific_name"])})
        return lineage_rank_data


def export_lineage_rank_to_csv(lineage_rank_data):
    df = pd.json_normalize(lineage_rank_data)
    df = df.drop(columns=["subclass", "superfamily", "superorder", "infraclass", "kingdom", "subphylum", "strain",
                          "subspecies", "suborder", "subfamily", "subkingdom", "section", "subgenus", "tribe",
                          "species subgroup", "no rank", "species group"])
    df.to_csv("data/disbiome_microbes_with_taxonomy_filtered.csv", index=False)
    return df


#     # export microbe-disease pairs to csv file
#     micro_dis_col = ["subject.scientific_name", "subject.taxid",
#                      "object.name", "object.mondo",
#                      "association.qualifier"]
#     micro_dis_df = df[micro_dis_col].copy()
#     micro_dis_df.rename(columns={"subject.scientific_name": "scientific_name",
#                                  "subject.taxid": "taxid",
#                                  "object.name": "object_name",
#                                  "object.mondo": "mondo",
#                                  "association.qualifier": "qualifier"},
#                         inplace=True)
#     micro_dis_df[["taxid"]] = micro_dis_df[["taxid"]].apply(convert_to_int)
#     micro_dis_df["scientific_name"] = micro_dis_df["scientific_name"].str.capitalize()
#     micro_dis_df.to_csv("disbiome_microbe_disease.csv", index=False)


if __name__ == "__main__":
    data = SaveData()
    if not os.path.exists("data/disbiome_output.pkl"):
        disbiome_pkl = data.save_disbiome_data_to_pkl("data/disbiome_output.pkl")

    manipulation = DataManipulation("data/disbiome_output.pkl")
    microbe_disease = manipulation.count_node_pair(node1="subject", node2="object", node_str1="scientific_name", node_str2="name")
    microbe_sample = manipulation.count_node_pair(node1="subject", node2="association", node_str1="scientific_name", node_str2="biospecimen_samples")
    print(microbe_disease)
    print(microbe_sample)

    mapped_taxids = manipulation.map_lineage_taxids()
    rank_info = manipulation.get_lineage_rank_data(mapped_taxids)
    print(export_lineage_rank_to_csv(rank_info))






