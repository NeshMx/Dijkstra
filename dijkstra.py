# Autor: Alejandro Huerta Campos - 14141111
# Materia: Administracion de Redes

# Librería para crear diccionarios con mejoras
from priodict import priorityDictionary

'''
    Función que recibe como parámetros:
        - Grafo predefinido
        - Nodo inicial
        - Nodo destino
        - Camino
    Retorna una lista de posibles caminos desde el nodo inicial al destino
'''


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def Dijkstra(G, start, end=None):
    D = {}  # dictionary of final distances
    P = {}  # dictionary of predecessors
    Q = priorityDictionary()  # estimated distances of non-final vertices
    Q[start] = 0

    for v in Q:
        D[v] = Q[v]
        if v == end:
            break

        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError(
                        "Dijkstra: se encotro un mejor camino al nodo destino.")
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return (D, P)


'''
    Función que recibe como parámetros:
        - Grafo predefinido
        - Nodo inicial
        - Nodo destino
    Retorna camino más corto desde el nodo inicial al destino
'''


def shortest_path(G, start, end):
    D, P = Dijkstra(G, start, end)
    Path = []
    while 1:
        Path.append(end)
        if end == start:
            break
        end = P[end]
    Path.reverse()
    return Path

# Grafos de prueba

# graph = {
#     'A': {'B': 10, 'D': 4, 'F': 10},
#     'B': {'E': 5, 'J': 10, 'I': 17},
#     'C': {'A': 4, 'D': 10, 'E': 16},
#     'D': {'F': 12, 'G': 21},
#     'E': {'G': 4},
#     'F': {'H': 3},
#     'G': {'J': 3},
#     'H': {'G': 3, 'J': 5},
#     'I': {},
#     'J': {'I': 8},
# }

# graph = {
#     'a': {'b': 10, 'c':5},
#     'b': {'c': 6},
# }


graph = {
    'A': {'B': 1, 'C': 2, 'D': 2},
    'B': {'A': 1, 'C': 5, 'D': 1},
    'C': {'A': 2, 'B': 5, 'D': 4, 'E': 2},
    'D': {'A': 2, 'B': 1, 'C': 4, 'E': 1},
    'E': {'C': 2, 'D': 1}
}

# Casos de prueba

start = input('Introduce el nodo inicial: ')
end = input('Introduce el nodo destino: ')

print("Caminos: \n" + "\n".join([str(i)
                                 for i in find_all_paths(graph, start, end)]))
print("Camino mas corto: " + " -> ".join([str(i)
                                          for i in shortest_path(graph, start, end)]))
