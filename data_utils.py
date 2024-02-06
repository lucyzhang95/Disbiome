import os
import pickle

import biothings_client
import pandas as pd

from disbiome_parser import load_disbiome_data


class SaveData:
    disbiome_data = None

    def __init__(self):
        self.disbiome_data = load_disbiome_data()

    def save_disbiome_data_to_pkl(self, output_path: str | os.PathLike) -> list:
        """
        Export disbiome data to pickle file
        :param output_path: "data/disbiome_output.pkl"
        :return: a list of full disbiome data dictionaries
        """
        parser_op = [obj for obj in self.disbiome_data]
        with open(output_path, "wb") as handle:
            pickle.dump(parser_op, handle, protocol=pickle.HIGHEST_PROTOCOL)
        return parser_op


class DataManipulation:
    def __init__(self, input_path: str | os.PathLike):
        """
        disbiome data from the pkl file
        :param input_path: "data/disbiome_output.pkl"
        """
        with open(input_path, "rb") as handle:
            self.disbiome_data = pickle.load(handle)

    def count_node_pair(self, node1: str, node2: str, node_str1: str, node_str2: str) -> str:
        """

        :param node1: string of dictionary key e.g. "object", "subject", "association"
        :param node2: string of dictionary key e.g. "object", "subject", "association"
        :param node_str1: string of the keys associated with the first node
        :param node_str2: string of the keys associated with the second node
        :return: count of unique pairs between node1 and node2
        """
        unique_pair = []
        for d in self.disbiome_data:
            if node_str1 in d[node1] and node_str2 in d[node2]:
                pair = f"{d[node1][node_str1]}-{d[node2][node_str2]}"
                unique_pair.append(pair)
        message = f"Number of unique pairs of {node1, node_str1}-{node2, node_str2}: {len(set(unique_pair))}"
        return message

    def map_lineage_taxids(self):
        """
        Acquire rank and scientific name using the lineage taxids from biothings_client "taxon"
        input is the disbiome_data taxids

        :return: a dictionary of taxid with its name and rank
        """
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

    def get_lineage_rank_data(self, mapped_lineage_taxids: dict) -> list:
        """
        Map the taxids to their lineage and obtain rank and scientific name
        Count the number of microbe-disease/biospecimen_samples pairs
        :param mapped_lineage_taxids: a dictionary of taxid as key and name + rank as values
        :return: a list of mapped lineage taxids, scientific name and rank
        """
        lineage_rank_data = []
        for d in self.disbiome_data:
            if (
                "taxid" in d["subject"]
                and "lineage" in d["subject"]
                and "parent_taxid" in d["subject"]
            ):
                microbe_d = {
                    "taxid": d["subject"]["taxid"],
                    "lineage": d["subject"]["lineage"],
                    "parent_taxid": d["subject"]["parent_taxid"],
                }
                lineage_rank_data.append(microbe_d)
        print(f"Number of records in mapped lineage data: {len(lineage_rank_data)}")

        for rank_d in lineage_rank_data:
            for taxid in rank_d["lineage"]:
                if taxid in mapped_lineage_taxids:
                    rank_d.update(
                        {
                            mapped_lineage_taxids[taxid]["rank"]: (
                                mapped_lineage_taxids[taxid]["scientific_name"]
                            )
                        }
                    )
        return lineage_rank_data


class ExportData:
    def __init__(self, lineage_rank_data: list):
        self.lineage_rank_data = lineage_rank_data

    def drop_columns(self, df: pd.DataFrame):
        """
        Static method to drop taxonomic rank columns
        :param df: pandas dataframe with taxonomic lineage taxids, scientific names and ranks
        :return: pandas dataframe after dropping selected taxonomic ranks
        """
        columns_to_drop = [
            "subclass",
            "superfamily",
            "superorder",
            "infraclass",
            "kingdom",
            "subphylum",
            "strain",
            "subspecies",
            "suborder",
            "subfamily",
            "subkingdom",
            "section",
            "subgenus",
            "tribe",
            "species subgroup",
            "no rank",
            "species group",
        ]
        df = df.drop(columns=columns_to_drop)
        return df

    def lineage_rank_to_csv(self, output_path: str | os.PathLike) -> pd.DataFrame:
        """

        :param output_path:
        :return:
        """
        df = pd.json_normalize(self.lineage_rank_data)
        df = self.drop_columns(df)
        # capitalize the phylum and species column
        df["phylum"] = df["phylum"].str.capitalize()
        df["species"] = df["species"].str.capitalize()
        df.to_csv(output_path, index=False)
        return df

    def microbe_disease_to_csv(
        self, disbiome_data: str | os.PathLike, output_path: str | os.PathLike
    ):
        lineage_rank = {d["taxid"]: d for d in self.lineage_rank_data}
        op_d = []
        with open(disbiome_data, "rb") as handle:
            disbiome_data = pickle.load(handle)
            for d in disbiome_data:
                if "name" in d["object"]:
                    pair_d = {"disease": d["object"]["name"]}
                if "biospecimen_samples" in d["association"]:
                    pair_d["biospecimen_samples"] = d["association"]["biospecimen_samples"]
                if "taxid" in d["subject"]:
                    if d["subject"]["taxid"] in lineage_rank:
                        pair_d.update(lineage_rank[d["subject"]["taxid"]])
                        op_d.append(pair_d)
                if "qualifier" in d["association"]:
                    pair_d["qualifier"] = d["association"]["qualifier"]
        print(f"Number of microbe-disease record: {len(op_d)}")

        df = pd.json_normalize(op_d)
        df = self.drop_columns(df)
        # capitalize the phylum and species
        df["phylum"] = df["phylum"].str.capitalize()
        df["species"] = df["species"].str.capitalize()
        # underlie the species
        df['species'] = df['species'].str.replace(' ', '_')
        df.to_csv(output_path, index=False)
        return df


if __name__ == "__main__":
    data = SaveData()
    if not os.path.exists("data/disbiome_output.pkl"):
        disbiome_pkl = data.save_disbiome_data_to_pkl("data/disbiome_output.pkl")

    manipulation = DataManipulation("data/disbiome_output.pkl")
    microbe_disease = manipulation.count_node_pair(
        node1="subject", node2="object", node_str1="scientific_name", node_str2="name"
    )
    microbe_sample = manipulation.count_node_pair(
        node1="subject",
        node2="association",
        node_str1="scientific_name",
        node_str2="biospecimen_samples",
    )
    print(microbe_disease)
    print(microbe_sample)
    mapped_taxids = manipulation.map_lineage_taxids()
    rank_info = manipulation.get_lineage_rank_data(mapped_taxids)
    # print(rank_info)

    export = ExportData(rank_info)
    taxonomy = export.lineage_rank_to_csv("data/disbiome_microbes_with_taxonomy_filtered.csv")
    microbe_disease_pair = export.microbe_disease_to_csv(
        disbiome_data="data/disbiome_output.pkl", output_path="data/disbiome_microbe_disease.csv"
    )
