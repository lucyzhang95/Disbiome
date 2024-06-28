import pandas as pd
import numpy as np
import random
import math

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.preprocessing import LabelEncoder

import matplotlib.pyplot as plt

import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import dendrogram, linkage

df = pd.read_csv("../data/disbiome_microbe_disease.csv")
df_disease = df.drop(columns=['taxid', 'lineage', 'parent_taxid', 'biospecimen_samples'])
df_taxon = df.drop(columns=['disease', 'taxid', 'lineage', 'parent_taxid', 'biospecimen_samples', 'qualifier'])

df_ibs = df_disease[df_disease["disease"].str.contains("irritable bowel syndrome")]
df_ibs = df_ibs.drop(columns=["superkingdom", "clade", "qualifier"]).dropna()


# phyla = df_disease["phylum"].unique()
# phyla_colors = {phylum: np.random.randint(0, 256) for phylum in phyla}
#
# df_disease["phylum_color"] = df_disease["phylum"].map(phyla_colors)
#
# df_encoded = pd.get_dummies(df_disease.drop(columns=['phylum_color']))
#
# lda = LDA(n_components=2)
# lda_components = lda.fit_transform(df_encoded, df_disease["disease"])
# lda_df = pd.DataFrame(lda_components, columns=[f"LD{i+1}" for i in range(2)])


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    """
    From Joel's answer at https://stackoverflow.com/a/29597209/2966723.
    Licensed under Creative Commons Attribution-Share Alike

    If the graph is a tree this will return the positions to plot this in a
    hierarchical layout.

    G: the graph (must be a tree)

    root: the root node of current branch
    - if the tree is directed and this is not given,
      the root will be found and used
    - if the tree is directed and this is given, then
      the positions will be just for the descendants of this node.
    - if the tree is undirected and not given,
      then a random choice will be used.

    width: horizontal space allocated for this branch - avoids overlap with other branches

    vert_gap: gap between levels of hierarchy

    vert_loc: vertical location of root

    xcenter: horizontal location of root
    """
    if not nx.is_tree(G):
        raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        """
        see hierarchy_pos docstring for most arguments

        pos: a dict saying where all nodes go if they have been assigned
        parent: parent of this branch. - only affects it if non-directed

        """

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


# TODO: the current version is not ideal, as it dropped all rows with na
# TODO: need to figure out a way to keep those rows
# Create a directed graph
G = nx.DiGraph()
for idx, row in df_ibs.iterrows():
    disease = row['disease']
    species = row['species']
    genus = row['genus']
    family = row['family']
    order = row['order']
    _class = row['class']
    phylum = row['phylum']

    G.add_node(disease)

    G.add_edges_from([(disease, phylum), (phylum, _class), (_class, order), (order, family), (family, genus), (genus, species)])


print(G.nodes)
plt.figure(figsize=(32, 24))
# Draw the networkx graph
# pos = hierarchy_pos(G, "irritable bowel syndrome")
# nx.draw(G, pos=pos, with_labels=True, node_size=1000, font_size=10, arrows=False)
# plt.show()

pos = hierarchy_pos(G, "irritable bowel syndrome", width=2*math.pi, xcenter=0)
new_pos = {u: (r*math.cos(theta), r*math.sin(theta)) for u, (theta, r) in pos.items()}
nx.draw(G, pos=new_pos, node_size=500, arrows=False, with_labels=True, font_size=16, node_color="orange")
nx.draw_networkx_nodes(G, pos=new_pos, nodelist=["irritable bowel syndrome"], node_color="blue", node_size=1000)

plt.show()
