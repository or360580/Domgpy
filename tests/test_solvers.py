from Pactapy.solvers import solve_example

def test_solve_example_empty():
    """Test that the solver handles empty input correctly."""
    assert solve_example([]) == [
        
    ]

def test_solve_example_data():
    """Test the solver with sample data."""
    data = [1, 2, 3]
    assert solve_example(data) == data




def analizar_grafica_aleatoria(n_nodos, probabilidad):
    # 1. Crear una gráfica aleatoria (Erdős-Rényi)
    # n = número de nodos, p = probabilidad de borde
    G = nx.erdos_renyi_graph(n_nodos, probabilidad)
    
    print(f"Grafica generada con {n_nodos} nodos y {G.number_of_edges()} aristas.")
    print("-" * 30)

    # 2. Conjunto de Dominación (Dominating Set)
    # Nota: NetworkX usa un algoritmo heurístico para encontrar un conjunto pequeño
    conjunto_dominacion = nx.dominating_set(G)
    numero_dominacion = len(conjunto_dominacion)
    
    print(f"Conjunto de Dominación: {conjunto_dominacion}")
    print(f"Número de Dominación (γ): {numero_dominacion}")
    print("-" * 30)

    # 3. Número Cromático (Coloración)
    # El algoritmo 'greedy_color' devuelve un diccionario de {nodo: color}
    dict_colores = nx.coloring.greedy_color(G, strategy="largest_first")
    # El número cromático es la cantidad de colores distintos usados
    num_cromatico = max(dict_colores.values()) + 1
    
    print(f"Número Cromático aproximado (χ): {num_cromatico}")
    print(f"Asignación de colores: {dict_colores}")

# --- Ejecución ---
# Generamos una gráfica de 10 nodos con un 30% de probabilidad de conexión
analizar_grafica_aleatoria(10, 0.3)