def dijkstra(graph, start, end):
    D = {}  # Diccionario de distancias finales
    P = {}  # Predeceso

    for node in list(graph):
        D[node] = -1  # Los vertices son inalcanzables
        P[node] = ""  # Los vertices no tienen predecesores

    D[start] = 0  # Nodo inicial

    unseen_nodes = list(graph)  # Lista de todos los nodos

    while len(unseen_nodes) > 0:
        # Selecciona el nodo con la menor distancia en D
        shortest = None
        node = ''
        for temp_node in unseen_nodes:
            if shortest == None:
                shortest = D[temp_node]
                node = temp_node
            elif D[temp_node] < shortest:
                shortest = D[temp_node]
                node = temp_node

        # El nodo seleccionado se remueve de la lista de nodos
        unseen_nodes.remove(node)

        for child_node, child_value in graph[node].items():
            if D[child_node] < D[node] + child_value:
                D[child_node] = D[node] + child_value
                P[child_node] = node

    # Creamos la lista de ruta
    path = []

    # Comenzamos desde el nodo destino
    node = end

    while not (node == start):
        if path.count(node) == 0:
            path.insert(0, node)  # Inserta el predecesor del nodo actual
            node = P[node]  # El nodo actual se convierte en predecesor
        else:
            break

    path.insert(0, start)  # Finalmente, se inserta el nodo inicial
    final_path = ' -> '.join(path)
    return final_path


def main():
    # Grafo de prueba
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

    print(dijkstra(graph, 'C', 'I'))


if __name__ == '__main__':
    main()
