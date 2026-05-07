"""Para esta prueba de codigo empezamos haciendo la importacion de la libreria Networkx."""
import networkx as nx
"""probaremos ahora haciendo la impotacion de una lubreria que pueda generar numeros aleatorios"""
import random

"""Aqui creamos una clase para hacer el analisis de las graficas."""
class AnalizadorGrafico:
    
    def __init__(self, n_nodes: int, aristas: float):
        self.n_nodes = n_nodes
        self.probability = aristas
        self.G = nx.erdos_renyi_graph(n_nodes, aristas)

    def get_domination_info(self):
        """Aqui llamamos al algoritmo que analiza la grafica y nos da el conjunto de dominacion."""
        dom_set = nx.dominating_set(self.G)
        return list(dom_set), len(dom_set)
    """Aqui definimos una funcion que nos da el número de clan (clique number) de la gráfica."""
    def get_clique_number(self):
        try:
            """En esta parte mandamos a llamar al algoritmo que viene en la libreria Networkx, este algoritmo nos da el numero de clan."""
            return nx.graph_clique_number(self.G)
        except AttributeError:
            """Esta parte nos da una aproximacion al numero de clan."""
            return len(nx.approximation.max_clique(self.G))

    """En esta parte definimos la funcion para calcular el numero de coloracion de la grafica."""
    def get_coloring_info(self):
        """Aqui mandamos a llamar el algoritmo que nos da el numero de coloracion."""
        coloring = nx.coloring.greedy_color(self.G, strategy="largest_first")
        chromatic_number = max(coloring.values()) + 1 if coloring else 0
        return coloring, chromatic_number

    def solve_example(self):
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
    """Aqui hacemos el codigo analizador."""
    if not data:
        return []
    analyzer = AnalizadorGrafico(n_nodes=len(data), probability=0.5)
    return analyzer.solve_example()

# --- EN ESTA PARTE PODEMOS MODIFICAR EL CODIGO PARA ASAIGNAR LOS NODOS Y ARISTAS ---
if __name__ == "__main__":
    n_nodos = 10
    p = 0.4
    analizador = AnalizadorGrafico(n_nodos, p)
    resultados = analizador.solve_example()

    print("=== Resultados del Análisis de Gráfica ===")
    for llave, valor in resultados.items():
        print(f"{llave.replace('_', ' ').capitalize()}: {valor}")