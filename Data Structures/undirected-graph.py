# Traversing an undirected graph

def buildGraph(edges):
    graph = {}

    for edge in edges:
        a, b = edge[0], edge[1]
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

def hasPath(graph, src, dst, visited):
    if src in visited:
        return False
    if src == dst:
        return True
    visited.add(src)
    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst, visited) == True:
            return True
    return False

def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, set())


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(undirectedPath(edges, 'i', 'k'))
