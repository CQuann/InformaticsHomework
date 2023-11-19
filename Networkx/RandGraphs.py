import networkx as nx
import matplotlib.pyplot as plt
from random import randint, shuffle

graph = nx.Graph()
dots = list("ABCDE")
edges = dots[:]
shuffle(edges)
for i in dots:
    graph.add_node(i)
for j in range(len(dots)):
    graph.add_edge(dots[j], edges[j], weight=randint(3, 15))
pos = nx.circular_layout(graph)
nx.draw(graph, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_weight)
plt.show()
