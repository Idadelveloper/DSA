# Find shortest path between two nodes in a graph fiven an edge list

def bulidGraph(edges):
  # Converts edge list to adjancency list
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


def shortestPath(edges, nodeA, nodeB):
    graph = bulidGraph(edges)
    visited = {nodeA}
    queue = [[nodeA, 0]]

    while len(queue) > 0:
        [node, distance] = queue.pop(0)
        if node == nodeB:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
            queue.append([neighbor, distance+1])
    return -1


edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

print(shortestPath(edges, 'w', 'z'))
