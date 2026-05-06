from Dompy.solvers import solve_example
"""Este  es un codigo de prueba donde definimos solo una funcion que nos genera de forma aleatoria una frafica, y en base a este buscamos el conjunto y el numero de dominacion."""
def test_solve_example_empty():
    assert solve_example([]) == [
        
    ]

def test_solve_example_data():
    data = [1, 2, 3]
    assert solve_example(data) == data



"""Aqui definimos nuestra funcion de analisis de grafica que depende de unicamente los nodos y las aristas"""
def an_graf_aleat(n_nodos, aristas):
    """Aqui la grafica la llamamos G, para generar la grafica usamos un algoritmo Erdos-Renyi que viene en la libreria de networkx """
    G = nx.erdos_renyi_graph(n_nodos, aristas)
    
    print(f"Grafica generada con {n_nodos} nodos y {G.number_of_edges()} aristas.")
    print("-" * 30)
    """el siguiente codigo manda a llamar un algoritmo que ya es contenido en la libreria Networkx"""
    conjunto_dominacion = nx.dominating_set(G)
    """El siguiente codigo ahora solamente hace el conteo de los elementos que estan en el conjunto de dominacion"""
    numero_dominacion = len(conjunto_dominacion)
    """Con los dos codigos anteriores obtenemos el conjunto de dominacion y el numero de dominacion."""

    
    print(f"Conjunto de Dominación: {conjunto_dominacion}")
    print(f"Número de Dominación (γ): {numero_dominacion}")
    print("-" * 30)

    """Este codigo esta demas sin embargo lo quise considerar para codigo de prueba en el grafico, donde nos da el numero cromatico"""
    dict_colores = nx.coloring.greedy_color(G, strategy="largest_first")
    num_cromatico = max(dict_colores.values()) + 1
    
    print(f"Número Cromático aproximado (χ): {num_cromatico}")
    print(f"Asignación de colores: {dict_colores}")
"""Por ultimo qui tenemos la designacion de cuantos nodos y aristas tendra nuestro grafo o grafica"""
an_graf_aleat(13, 0.3)