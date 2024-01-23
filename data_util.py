# from disbiome_parser import load_disbiome_data
import pickle

import pandas as pd
import numpy as np


# all_data = []
# data = load_disbiome_data()
# for obj in data:
#     print(obj)
#     all_data.append(obj)
# with open("disbiome_output.pkl", "wb") as handle:
#     pickle.dump(all_data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def convert_to_int(val):
    return pd.to_numeric(val, errors='coerce').astype('Int64')


with open("disbiome_output.pkl", "rb") as handle:
    data = pickle.load(handle)
    df = pd.json_normalize(data)

    # export microbes related info to csv file
    microbe_col = ["subject.scientific_name", "subject.taxid", "subject.lineage", "subject.parent_taxid", "subject.rank"]
    microbe_df = df[microbe_col].copy()
    microbe_df.rename(columns={"subject.scientific_name": "scientific_name",
                               "subject.taxid": "taxid",
                               "subject.lineage": "lineage",
                               "subject.parent_taxid": "parent_taxid",
                               "subject.rank": "rank"},
                      inplace=True)
    col_to_convert = ["taxid", "parent_taxid"]
    microbe_df[col_to_convert] = microbe_df[col_to_convert].apply(convert_to_int)
    microbe_df["rank"] = microbe_df["rank"].replace('', pd.NA)
    microbe_df["scientific_name"] = microbe_df["scientific_name"].str.capitalize()
    microbe_df.to_csv("disbiome_microbes.csv", index=False)

    # export microbe-disease pairs to csv file
    micro_dis_col = ["subject.scientific_name", "subject.taxid",
                     "object.name", "object.mondo",
                     "association.qualifier"]
    micro_dis_df = df[micro_dis_col].copy()
    micro_dis_df.rename(columns={"subject.scientific_name": "scientific_name",
                                 "subject.taxid": "taxid",
                                 "object.name": "object_name",
                                 "object.mondo": "mondo",
                                 "association.qualifier": "qualifier"},
                        inplace=True)
    micro_dis_df[["taxid"]] = micro_dis_df[["taxid"]].apply(convert_to_int)
    micro_dis_df["scientific_name"] = micro_dis_df["scientific_name"].str.capitalize()
    micro_dis_df.to_csv("disbiome_microbe_disease.csv", index=False)


