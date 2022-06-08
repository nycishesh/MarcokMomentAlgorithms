
### IMPORTS
import networkx as nx                  # NetworkX should be imported as nx
import matplotlib.pyplot as plt     # Matplotlib should be imported as plt


### GRAPH
G = nx.DiGraph()


### ADDING NODES 
nodes_in_G = {
    '0' : {},
    '1' : {},
    '2' : {},
    '3' : {},
    '4' : {},
    '5' : {},
    '6' : {}
}

for node in nodes_in_G:
    G.add_node(
        node,
    )



### ADDING EDGES
edges_in_G = {
    '0' : [('1', 10), ('5', 20)],
    '1' : [('2', 30), ('4', 5), ('3', 17), ('2', 13)],
    '2' : [('3', 13)],
    '3' : [('1', 17), ('0', 13)],
    '4' : [('3', 20), ('6', 1)],
    '5' : [('4', 7)]
}

for u in edges_in_G:
    for connection in edges_in_G[u]:
        G.add_edge(
            u,
            connection[0],
            weight= connection[1])

### WORK



### DRAWING 
nx.draw(
    G,
    pos = nx.circular_layout(G),
    with_labels = True,
)

plt.show()