import networkx as nx
import matplotlib.pyplot as plt

"""Crearemos aqui una clase para nuestra funcion de analisis del grafico o Grafo."""
class Grap_An:

    def  __init__(self):
        """Mandamos a llamar un grafico de Peterson de nuestra libreria Networkx"""
        self.G = nx.peterson_graph()
        self.n_nodes = self.G.nnumber_of_nodes()

    def is_dominating_set(self, candidate_set):
        """Verifica si un conjunto de nodos es un conjunto dominante."""
        covered = set(candidate_set)
        for node in candidate_set:
            covered.update(self.G.neighbors(node))
        return len(covered) == self.n_nodes

    def get_domination_info(self):
        """Calcula el conjunto y número de dominación usando Backtracking."""
        # Todos los nodos en el grafo de Petersen tienen grado 3, por lo que el orden
        # inicial es simplemente la lista de nodos del 0 al 9.
        nodes = list(self.G.nodes())
        
        best_dom_set = nodes[:]  # Inicialmente, el peor caso (todos los nodos)
        min_size = len(nodes)

        def backtrack(index, current_set):
            nonlocal best_dom_set, min_size

            # Poda (Pruning): Si el conjunto actual ya es igual o mayor al mejor encontrado, 
            # no tiene sentido seguir explorando esta rama.
            if len(current_set) >= min_size:
                return

            # Si el conjunto actual es dominante, guardamos el nuevo mínimo
            if self.is_dominating_set(current_set):
                best_dom_set = current_set.copy()
                min_size = len(current_set)
                return

            # Si ya revisamos todos los nodos, terminamos esta rama
            if index == len(nodes):
                return

            # Opción 1: Incluir el nodo actual en el conjunto
            current_set.append(nodes[index])
            backtrack(index + 1, current_set)
            current_set.pop()  # Retroceder (Backtrack)

            # Opción 2: No incluir el nodo actual
            backtrack(index + 1, current_set)

        # Iniciar el backtracking desde el índice 0 con un conjunto vacío
        backtrack(0, [])
        return best_dom_set, min_size

    def get_clique_number(self):
        """Calcula el número de clan (clique)."""
        try:
            return nx.graph_clique_number(self.G)
        except AttributeError:
            return len(nx.approximation.max_clique(self.G))

    def get_coloring_info(self):
        """Calcula la coloración y el número cromático."""
        coloring = nx.coloring.greedy_color(self.G, strategy="largest_first")
        chromatic_number = max(coloring.values()) + 1 if coloring else 0
        return coloring, chromatic_number

    def show_graph(self, title="Análisis del Grafo de Petersen"):
        """Genera una ventana visual con la clásica forma del Grafo de Petersen."""
        coloring, _ = self.get_coloring_info()
        node_colors = [coloring.get(node, 0) for node in self.G.nodes()]
        
        plt.figure(figsize=(8, 8))
        
        # Para dibujar el Grafo de Petersen en su forma icónica,
        # posicionamos los nodos en dos capas concéntricas (shells):
        # Capa exterior: nodos [0, 1, 2, 3, 4]
        # Capa interior: nodos [5, 6, 7, 8, 9]
        pos = nx.shell_layout(self.G, nlist=[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
        
        nx.draw(
            self.G, pos, 
            with_labels=True, 
            node_color=node_colors, 
            cmap=plt.cm.rainbow, 
            node_size=800,
            font_size=12,
            font_color="white",
            font_weight="bold",
            edge_color='gray',
            width=2.0
        )
        
        plt.title(title, fontsize=14, fontweight="bold")
        plt.show()

    def solve_example(self):
        """Método unificado para retornar los resultados del grafo."""
        dom_set, dom_num = self.get_domination_info()
        coloring, chrom_num = self.get_coloring_info()
        clique_num = self.get_clique_number()
        
        return {
            "nodos": self.n_nodes,
            "aristas": self.G.number_of_edges(),
            "conjunto_dominacion": dom_set,
            "numero_dominacion": dom_num,
            "numero_clan": clique_num,impor
            "numero_cromatico": chrom_num
        }

# --- BLOQUE DE EJECUCIÓN ---
if __name__ == "__main__":
    print("--- Análisis de Grafo Especial: Grafo de Petersen ---")
    
    # Instanciamos el analizador para el grafo de Petersen (no requiere parámetros de entrada)
    analizador = GraphAnalyzer()
    
    # 1. Mostrar datos en consola
    resultados = analizador.solve_example()
    print("\n=== Resultados del Análisis ===")
    for llave, valor in resultados.items():
        print(f"{llave.capitalize().replace('_', ' ')}: {valor}")
    
    # 2. Mostrar la gráfica de Petersen con su dibujo geométrico clásico
    print("\nGenerando visualización geométrica del Grafo de Petersen...")
    analizador.show_graph("El Grafo de Petersen (Coloración Mínima)")    