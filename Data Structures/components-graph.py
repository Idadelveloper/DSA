def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True


def connectedComponentsCount(graph):
    """
    Counts the number of connected nodes
    """
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited) == 0:
            count += 1
    return count

def exploreSize(graph, node, visited):
    if node in visited:
        return 0

    visited.add(node)

    size = 1
    for neighbor in graph[node]:
        size += exploreSize(graph, neighbor, visited)
    return size

def largestComponent(graph):
    visited = set()
    longest = 0
    for node in graph:
        size = exploreSize(graph, node, visited)
        if size > longest:
            longest = size
    return longest


components = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

print(connectedComponentsCount(components))
print(largestComponent(components))
