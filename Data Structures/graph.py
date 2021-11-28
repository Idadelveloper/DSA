def depthFirstPrint(graph, source):
    ''' Graph depth first traversal iteratively '''
    stack = [source]

    while len(stack) > 0:
        current = stack.pop()
        print(current)
        graph[current]
        for neighbor in graph[current]:
            stack.append(neighbor)

def depthFirstPrintRecur(graph, source):
    ''' Graph depth first search traversal recursively '''
    print(source)
    for neighbor in graph[source]:
        depthFirstPrint(graph, neighbor)

def breadthFirstPrint(graph, source):
    queue = [source]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

def hasPath(graph, src, dst):
    ''' 
    Considering the graph is acyclic, 
    check if path exists using depth first search
    '''
    if src == dst:
        return True

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dst) == True:
            return True
    return False

def hasPathBF(graph, src, dst):
    ''' Finding if graph has path using breadth frist search '''
    queue = [src]
    while len(queue) > 0:
        current = queue.pop(0)
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": []
}

depthFirstPrint(graph, 'a')
print("----------")
depthFirstPrintRecur(graph, 'a')
print("----------")
breadthFirstPrint(graph, 'a')
print(hasPath(graph, 'a', 'g'))
print(hasPathBF(graph, 'a', 'g'))

