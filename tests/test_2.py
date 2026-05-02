##Para empezqar tengamos la implementacion de la libreria solicitada.
import networkx as nx
import matplotlib.pyplot as plt
## aqui hacemos una funcion para generar el grafo de forma aleatoria, dados los nodos y la probabilidad
def generar_grafo_aleatorio(n_nodos, probabilidad):
    G = nx.erdos_renyi_graph(n_nodos, probabilidad)
    
    ###En esta parte del codigo planeamos hacer que se haga la impresion del grafo 
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', node_size=500)
    plt.title(f"Grafo Aleatorio (n={n_nodos}, p={probabilidad})")
    plt.show()

    return G

###Este codigo lo podemos modificar para seleccionar el numero de nodos y la probabilidad de enlaece de nuestro grafo.
mi_grafo = generar_grafo_aleatorio(15, 0.2)