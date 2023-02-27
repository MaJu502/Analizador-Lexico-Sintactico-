# Universidad del Valle de Guatemala
# Marco Jurado 20308
from graphviz import Digraph

def graficarAutom(automata):
    estados = automata[0]
    inicial = automata[1].pop()
    final = automata[2]
    transiciones = automata[3]

    graph = Digraph()
    graph.attr(rankdir='LR')

    for nodo in estados:
        if nodo == inicial:
            graph.node(str(nodo), shape='circle', fillcolor='lightgreen', style='filled')
        
        elif nodo in final:
            graph.node(str(nodo), shape='doublecircle', fillcolor='lightred', style='filled')
        
        else: 
            graph.node(str(nodo), shape='circle')

    for i, (from_state, to_state, symbol) in enumerate(transiciones):
        graph.edge(str(from_state), str(to_state), label=symbol, arrowhead='vee')


    graph.render()