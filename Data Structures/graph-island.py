import math

def explore(grid, r, c, visited):
    rowInbounds = 0 <= r and r < len(grid)
    colInbounds = 0 <= c and c < len(grid[0])
    if not rowInbounds or not colInbounds:
        return False
    if grid[r][c] == 'W':
        return False

    pos = str(r) + ',' + str(c)
    if pos in visited:
        return False
    visited.add(pos)

    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c+1, visited)
    explore(grid, r, c-1, visited)

    return True

def islandCount(grid):
  """
  Counts the number of islands given a grid
  """
    visited = set()
    count = 0
    for r in range(0, len(grid)+1):
        for c in range(0, len(grid[0]) + 1):
            if explore(grid, r, c, visited) == True:
                count += 1
    return count

def exploreSize(grid, r, c, visited):
    rowInbounds = 0 <= r and r < len(grid)
    colInbounds = 0 <= c and c < len(grid[0])
    if not rowInbounds or not colInbounds:
        return 0

    if grid[r][c] == 'W':
        return 0

    pos = str(r) + "," + str(c)
    if pos in visited:
        return 0
    visited.add(pos)

    size = 1
    size += exploreSize(grid, r-1, c, visited)
    size += exploreSize(grid, r+1, c, visited)
    size += exploreSize(grid, r, c-1, visited)
    size += exploreSize(grid, r, c+1, visited)

    return size


def minimumIsland(grid):
  # Finds the size of the smallest island
    visited = set()
    minSize = math.inf
    for r in range(0, len(grid)+1):
        for c in range(0, len(grid[0]) + 1):
            size = exploreSize(grid, r, c, visited)
            if size > 0 and size < minSize:
                minSize = size
    return minSize
    




grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

print(islandCount(grid))
print(minimumIsland(grid))
