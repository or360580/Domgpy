"""Empezamos haciendo la implementacion de la libreria Networkx"""
import networkx as nx
"""Aqui cargamos una libreria que nos va a ayudar a visualizar el grafico que queramos generar"""
import matplotlib.pyplot as plt

"""En esta parte definimos la funcion para la cual nos generara el grafico de forma aleatoria"""
def grafo_aleatorio(n_nodos, aristas):
    """Aqui mandamos llamar el algoritmo contenido en nuestra libreria de Networkx que nos ayudara a generar nuestro grafo"""
    G = nx.erdos_renyi_graph(n_nodos, aristas)
    
    """En esta parte llamamos los algoritmos que nos daran la imagen de nuestro grafo los cuales estan contenidos en la libreria Matplot que implementemos despues de la libreria networkx"""
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=True, node_color='skyblue', edge_color='gray', node_size=500)
    plt.title(f"Grafo Aleatorio (n={n_nodos}, p={aristas})")
    plt.show()

    return G

"""Este codigo lo podemos modificar para seleccionar el numero de nodos y las aristas qeu tendra nuestro grafo.""" 
mi_grafo = grafo_aleatorio(15, 0.2)