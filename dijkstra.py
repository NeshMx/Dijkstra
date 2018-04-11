from priodict import priorityDictionary


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
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
                        "Dijkstra: found better path to already-final vertex")
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return (D, P)


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


graph = {
    'A': {'B': 10, 'D': 4, 'F': 10},
    'B': {'E': 5, 'J': 10, 'I': 17},
    'C': {'A': 4, 'D': 10, 'E': 16},
    'D': {'F': 12, 'G': 21},
    'E': {'G': 4},
    'F': {'H': 3},
    'G': {'J': 3},
    'H': {'G': 3, 'J': 5},
    'I': {},
    'J': {'I': 8},
}

print("Caminos: \n" + "\n".join([str(i) for i in find_all_paths(graph, 'A', 'J')]))
print("Camino mas corto: " + " -> ".join([str(i) for i in shortest_path(graph, 'A', 'J')]))
