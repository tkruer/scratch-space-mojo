
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:            
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


print(bfs(
    graph={
        'a': {'b', 'c'},
        'b': {'a', 'd'},
        'c': {'a', 'd', 'e'},
        'd': {'e'},
        'e': {'c', 'f'},
        'f': {'e'}
    },
    start='a'
))
