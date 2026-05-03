import networkx as nx
import random

class GraphAnalyzer:
    """Clase para generar y analizar propiedades teóricas de gráficas."""
    
    def __init__(self, n_nodes: int, probability: float):
        self.n_nodes = n_nodes
        self.probability = probability
        # Generar gráfica aleatoria Erdős-Rényi
        self.G = nx.erdos_renyi_graph(n_nodes, probability)

    def get_domination_info(self):
        """Calcula el conjunto y número de dominación."""
        dom_set = nx.dominating_set(self.G)
        return list(dom_set), len(dom_set)

    def get_clique_number(self):
        """Calcula el número de clan (clique number) de la gráfica."""
        return nx.graph_clique_number(self.G)

    def get_coloring_info(self):
        """Calcula la coloración greedy y el número cromático."""
        coloring = nx.coloring.greedy_color(self.G, strategy="largest_first")
        chromatic_number = max(coloring.values()) + 1 if coloring else 0
        return coloring, chromatic_number

    def solve_example(self):
        """Método unificado para retornar los resultados en un formato estructurado."""
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
    """Función de conveniencia para compatibilidad con tus tests."""
    if not data:
        return []
    # Usamos el primer valor como n_nodes y una probabilidad fija o aleatoria
    analyzer = GraphAnalyzer(n_nodes=len(data), probability=0.5)
    return analyzer.solve_example()