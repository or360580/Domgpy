 import networkx as nx
import random

class GraphAnalyzer:
    """Clase para generar y analizar propiedades teóricas de gráficas."""
    
    def __init__(self, n_nodes: int, probability: float):
        # CORRECCIÓN: Usar n_nodes (el parámetro de la función)
        self.n_nodes = n_nodes
        self.probability = probability
        # CORRECCIÓN: Usar self.n_nodes para generar el grafo
        self.G = nx.erdos_renyi_graph(n_nodes, probability)

    def get_domination_info(self):
        """Calcula el conjunto y número de dominación."""
        dom_set = nx.dominating_set(self.G)
        return list(dom_set), len(dom_set)

    def get_clique_number(self):
        """Calcula el número de clan (clique number) de la gráfica."""
        # Nota: En versiones muy nuevas de NetworkX esto se movió a nx.approximation
        try:
            return nx.graph_clique_number(self.G)
        except AttributeError:
            return len(nx.approximation.max_clique(self.G))

    def get_coloring_info(self):
        """Calcula la coloración greedy y el número cromático."""
        coloring = nx.coloring.greedy_color(self.G, strategy="largest_first")
        chromatic_number = max(coloring.values()) + 1 if coloring else 0
        return coloring, chromatic_number

    def solve_example(self):
        """Método unificado para retornar los resultados."""
        dom_set, dom_num = self.get_domination_info()
        coloring, chrom_num = self.get_coloring_info()
        clique_num = self.get_clique_number()
        
        return {
            "nodos": self.n_nodes,
            "aristas": self.G.number_of_edges(),
            "conjunto_dominacion": dom_set,
            "numero_dominacion": dom_num,
            "numero_clan": clique_num,
            "numero_cromatico": chrom_num,
            "coloracion": coloring
        }

def solve_example(data):
    """Función para compatibilidad con tests."""
    if not data:
        return []
    analyzer = GraphAnalyzer(n_nodes=len(data), probability=0.5)
    return analyzer.solve_example()

# --- BLOQUE DE EJECUCIÓN (Fuera de las funciones) ---
if __name__ == "__main__":
    n_nodos = 10
    p = 0.4
    analizador = GraphAnalyzer(n_nodos, p)
    resultados = analizador.solve_example()

    print("=== Resultados del Análisis de Gráfica ===")
    for llave, valor in resultados.items():
        print(f"{llave.replace('_', ' ').capitalize()}: {valor}")