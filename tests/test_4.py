"""En este codigo de prueba ya haremos directamente la implementacion de las 3 librerias que consideraremos usar para el codigo, una contiene los algoritmos de resolucion, la otra nos dibujara el grafico y la ultima es para generar de forma aleatoria."""
import networkx as nx
import matplotlib.pyplot as plt
import random

class AnGrap:
    """Clase para generar, analizar y visualizar propiedades de gráficas."""
    
    def __init__(self, n_nodes: int, probability: float):
        self.n_nodes = n_nodes
        self.probability = probability
        self.G = nx.erdos_renyi_graph(n_nodes, probability)

    def get_domination_info(self):
        """Calcula el conjunto y número de dominación."""
        dom_set = nx.dominating_set(self.G)
        return list(dom_set), len(dom_set)

    def get_clique_number(self):
        """Calcula el número de clan."""
        try:
            return nx.graph_clique_number(self.G)
        except AttributeError:
            return len(nx.approximation.max_clique(self.G))

    def get_coloring_info(self):
        """Calcula la coloración y el número cromático."""
        coloring = nx.coloring.greedy_color(self.G, strategy="largest_first")
        chromatic_number = max(coloring.values()) + 1 if coloring else 0
        return coloring, chromatic_number

    def show_graph(self, title="Análisis de Gráfica Aleatoria"):
        """Genera una ventana visual con la gráfica coloreada."""
        coloring, _ = self.get_coloring_info()
        
        node_colors = [coloring.get(node, 0) for node in self.G.nodes()]
        
        plt.figure(figsize=(10, 7))
        pos = nx.spring_layout(self.G)
        
        nx.draw(
            self.G, pos, 
            with_labels=True, 
            node_color=node_colors, 
            cmap=plt.cm.rainbow,
            node_size=600,
            edge_color='lightgray'
        )
        
        plt.title(title)
        plt.show()

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
            "numero_cromatico": chrom_num
        }

# --- BLOQUE DE EJECUCIÓN ---
if __name__ == "__main__":
    n_nodos = 12
    p = 0.3
    
    analizador = AnGrap(n_nodos, p)
    
    # 1. Mostrar datos en consola
    resultados = analizador.solve_example()
    print("=== Resultados del Análisis ===")
    for llave, valor in resultados.items():
        print(f"{llave.capitalize()}: {valor}")
    
    # 2. MOSTRAR LA GRÁFICA
    analizador.show_graph(f"Grafo Aleatorio (n={n_nodos}, p={p})")