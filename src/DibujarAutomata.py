# Universidad del Valle de Guatemala
# Marco Jurado 20308
import networkx as nx
import matplotlib.pyplot as plt

def graficarAutom(automata):
    estados = automata[0]
    inicial = automata[1].pop()
    final = automata[2]
    transiciones = automata[3]
    graph = nx.DiGraph()

    for nodo in estados:
        graph.add_node(nodo)

    for i, (from_state, to_state, symbol) in enumerate(transiciones):
        graph.add_edge(from_state, to_state, label=symbol)

    graph.nodes[inicial]['color'] = 'green'

    for j in final:
        graph.nodes[j]['color'] = 'red'
        graph.nodes[j]['shape'] = 'doubleCircle'

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels = True, arrowstyle='->')
    labels = nx.get_edge_attributes(graph,'label')
    nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
    plt.show()