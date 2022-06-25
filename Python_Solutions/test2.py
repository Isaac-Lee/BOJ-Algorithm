from collections import deque

def neighbors(current, grid):
    x, y = current
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                yield i, j

def bfs(grid, start, end):
    queue = deque([start])
    visited = {start}
    while queue:
        current = queue.popleft()
        if current == end:
            return True
        for next in neighbors(current, grid):
            if next not in visited:
                visited.add(next)
                queue.append(next)
    return False
