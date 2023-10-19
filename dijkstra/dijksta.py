def dijkstra(graph, start):
    shortest_path = {}
    predecessor = {}
    unseen_nodes = graph
    infinity = float('inf')
    path = []
    for node in unseen_nodes:
        shortest_path[node] = infinity
    shortest_path[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_path[node] < shortest_path[min_node]:
                min_node = node

        path_options = graph[min_node].items()
        for child_node, weight in path_options:
            if weight + shortest_path[min_node] < shortest_path[child_node]:
                shortest_path[child_node] = weight + shortest_path[min_node]
                predecessor[child_node] = min_node
        unseen_nodes.pop(min_node)

    return shortest_path

print(dijkstra(
    graph={
        'a': {'b': 10, 'c': 3},
        'b': {'c': 1, 'd': 2},
        'c': {'b': 4, 'd': 8, 'e': 2},
        'd': {'e': 7},
        'e': {'d': 9}
    },
    start='a'
))