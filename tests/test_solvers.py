import unittest
import networkx as nx
from Dompy.solvers import GraphAnalyzer

class TestGraphAnalyzer(unittest.TestCase):
    """Suite de pruebas unitarias para la clase GraphAnalyzer."""

    def setUp(self):
        """Método de configuración que se ejecuta antes de cada prueba."""
        self.analizador = GraphAnalyzer()

    def test_inicializacion_grafo_petersen(self):
        """Verifica que el grafo cargado sea el de Petersen (10 nodos, 15 aristas)."""
        self.assertEqual(self.analizador.n_nodes, 10, "El Grafo de Petersen debe tener exactamente 10 nodos.")
        self.assertEqual(self.analizador.G.number_of_edges(), 15, "El Grafo de Petersen debe tener exactamente 15 aristas.")
        
        # Verificar que sea un grafo 3-regular (todos los nodos con grado 3)
        for node in self.analizador.G.nodes():
            self.assertEqual(self.analizador.G.degree(node), 3, f"El nodo {node} debe tener grado 3.")

    def test_verificacion_conjunto_dominante_valido(self):
        """Prueba que el método de validación identifique correctamente un conjunto dominante real."""
        # {0, 2, 6} es un conjunto dominante mínimo verídico para el Grafo de Petersen
        conjunto_valido = [0, 2, 6]
        self.assertTrue(
            self.analizador.is_dominating_set(conjunto_valido),
            "El conjunto {0, 2, 6} debería ser identificado como un conjunto dominante válido."
        )

    def test_verificacion_conjunto_dominante_invalido(self):
        """Prueba que el método de validación rechace un conjunto que no domina a todo el grafo."""
        # Un conjunto de 2 elementos nunca puede dominar los 10 nodos del Grafo de Petersen
        conjunto_invalido = [0, 1]
        self.assertFalse(
            self.analizador.is_dominating_set(conjunto_invalido),
            "Un conjunto de tamaño 2 no puede dominar el Grafo de Petersen."
        )

    def test_algoritmo_backtracking_dominacion(self):
        """Prueba que el algoritmo de backtracking devuelva los valores teóricos correctos."""
        conjunto_dom, numero_dom = self.analizador.get_domination_info()
        
        # El número de dominación teórica de Petersen es exactamente 3
        self.assertEqual(numero_dom, 3, "El número de dominación de Petersen debe ser exactamente 3.")
        
        # Validar que el conjunto devuelto por el backtracking sea realmente dominante
        self.assertTrue(
            self.analizador.is_dominating_set(conjunto_dom),
            "El conjunto óptimo encontrado por backtracking debe ser un conjunto dominante."
        )
        
        # El tamaño del conjunto debe coincidir con el número devuelto
        self.assertEqual(len(conjunto_dom), 3, "La cardinalidad del conjunto dominante debe ser 3.")

    def test_numero_de_clan(self):
        """Verifica que el número de clan (clique number) calculado sea correcto (2)."""
        clique_num = self.analizador.get_clique_number()
        # El Grafo de Petersen no tiene triángulos, por lo que su clan máximo es una arista (K_2)
        self.assertEqual(clique_num, 2, "El número de clan del Grafo de Petersen debe ser exactamente 2.")

    def test_coloracion_y_numero_cromatico(self):
        """Prueba la coloración óptima (3-coloración)."""
        colores, num_cromatico = self.analizador.get_coloring_info()
        
        # El número cromático mínimo de Petersen es exactamente 3
        self.assertEqual(num_cromatico, 3, "El número cromático del Grafo de Petersen debe ser exactamente 3.")
        
        # Validar la regla de coloración: ningún nodo vecino debe tener el mismo color
        for u, v in self.analizador.G.edges():
            self.assertNotEqual(
                colores[u], colores[v],
                f"Conflicto de coloración: los nodos conectados {u} y {v} comparten el color {colores[u]}."
            )
    def test_solve_example(self):
        """Verifica que el método solve_example retorne la estructura de datos unificada correcta."""
        resultados = self.analizador.solve_example()
        
        # Asegurar que devuelva un diccionario
        self.assertIsInstance(resultados, dict, "solve_example debe retornar un diccionario.")
        
        # Verificar la existencia de todas las llaves esperadas en el reporte unificado
        llaves_esperadas = {
            "nodos", "aristas", "conjunto_dominacion", 
            "numero_dominacion", "numero_clan", "numero_cromatico"
        }
        self.assertTrue(llaves_esperadas.issubset(resultados.keys()), "El diccionario de resultados no contiene todas las llaves requeridas.")
        
        # Validar que los valores internos sigan las propiedades del Grafo de Petersen
        self.assertEqual(resultados["nodos"], 10, "El valor de 'nodos' en solve_example debe ser 10.")
        self.assertEqual(resultados["aristas"], 15, "El valor de 'aristas' en solve_example debe ser 15.")
        self.assertEqual(resultados["numero_dominacion"], 3, "El valor de 'numero_dominacion' en solve_example debe ser 3.")
        self.assertEqual(resultados["numero_clan"], 2, "El valor de 'numero_clan' en solve_example debe ser 2.")
        self.assertEqual(resultados["numero_cromatico"], 3, "El valor de 'numero_cromatico' en solve_example debe ser 3.")
        
        # Validar que el conjunto de dominación devuelto sea realmente dominante
        self.assertTrue(
            self.analizador.is_dominating_set(resultados["conjunto_dominacion"]),
            "El conjunto dentro de 'conjunto_dominacion' debe dominar al grafo."
        )
            