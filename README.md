# Domgpy
Problemas de dominacion en Graficas. 
Utilizamos las siguientes librerias de python:
-Networkx(la principal para sacar los algoritmos de resolucion que ocpamos en el problema.)
-MAtplot(Esta se la agregamos para que se pueda isualizar nuestra grafica.)
-Ramdom(como su nombre lo indica lo usaremos para generar objeto de forma aleatoria.).
dentro de los problemas de dominacion tenemos lo que es el numero de dominacio que en pocas palabras podremos interpretarlo como el numero de elementos contenidos en nuestro "conjunto de dominacion".
A continuacion tengamos una descripcion del problema que se nos presenta en este codigo o algoritmo de solucion.

## Número de Dominación y Conjunto Dominante en Teoría de Grafos

### Conjunto Dominante (Dominating Set)

Un **conjunto dominante** en un grafo G = (V, E) es un subconjunto D ⊆ V de vértices tal que todo vértice que no está en D es **adyacente a al menos un vértice en D**.

En otras palabras: para cada vértice v ∈ V \ D, existe al menos un vértice u ∈ D tal que existe una arista entre u y v.

#### Ejemplo
En un grafo simple:
```
    1 --- 2
    |     |
    3 --- 4
```
El conjunto D = {2, 3} es un conjunto dominante porque:
- El vértice 1 es adyacente a 2 y 3 ✓
- El vértice 2 está en D ✓
- El vértice 3 está en D ✓
- El vértice 4 es adyacente a 2 y 3 ✓

### Número de Dominación (Domination Number)

El **número de dominación** γ(G) de un grafo G es la **cardinalidad (tamaño) del conjunto dominante más pequeño**.

γ(G) = min{|D| : D es un conjunto dominante de G}

En el ejemplo anterior, γ(G) = 2 porque:
- El conjunto mínimo dominante tiene 2 vértices
- No existe un conjunto dominante de 1 solo vértice

### Propiedades Importantes

1. **Trivialidad**: Todo grafo tiene al menos un conjunto dominante (el conjunto de todos los vértices)
2. **Minimalidad**: Un conjunto dominante es **minimal** si ningún subconjunto propio es también dominante
3. **NP-completitud**: Encontrar el número de dominación es un problema NP-completo

### Aplicaciones Prácticas

- **Redes de vigilancia**: Posicionamiento mínimo de cámaras
- **Redes informáticas**: Ubicación óptima de servidores
- **Protección de sistemas**: Cobertura mínima de nodos críticos 
