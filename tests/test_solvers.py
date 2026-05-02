from Dompy.solvers import solve_example

def test_solve_example_empty():
    assert solve_example([]) == [
        
    ]

def test_solve_example_data():
    data = [1, 2, 3]
    assert solve_example(data) == data




def analizar_grafica_aleatoria(n_nodos, probabilidad):
    G = nx.erdos_renyi_graph(n_nodos, probabilidad)
    
    print(f"Grafica generada con {n_nodos} nodos y {G.number_of_edges()} aristas.")
    print("-" * 30)
    conjunto_dominacion = nx.dominating_set(G)
    numero_dominacion = len(conjunto_dominacion)
    
    print(f"Conjunto de Dominación: {conjunto_dominacion}")
    print(f"Número de Dominación (γ): {numero_dominacion}")
    print("-" * 30)

    dict_colores = nx.coloring.greedy_color(G, strategy="largest_first")
    num_cromatico = max(dict_colores.values()) + 1
    
    print(f"Número Cromático aproximado (χ): {num_cromatico}")
    print(f"Asignación de colores: {dict_colores}")

analizar_grafica_aleatoria(10, 0.3)