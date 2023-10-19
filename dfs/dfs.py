def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
    return visited

print(dfs(
    graph={
        'a': {'b', 'c'},
        'b': {'a', 'd'},
        'c': {'a', 'd', 'e'},
        'd': {'e'},
        'e': {'c', 'f'},
        'f': {'e'}
    },
    node='a',
    visited=set()
))