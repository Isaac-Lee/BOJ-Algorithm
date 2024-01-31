from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def is_in_graph(x, y, n, m):
  if x < 0 or y < 0 or x >= n or y >= m:
    return False
  else:
    return True
  
def can_go(visit, graph, x, y):
  if graph[x][y] == 0:
    return False
  elif (x, y) in visit:
    return False
  else:
    return True

def BFS(start, graph, n, m):
  visit = set()
  queue = deque()
  queue.append(start)
  
  while queue:
    current = queue.popleft()
    visit.add(current)
    x, y = current
    graph[x][y] += 1
    for i in range(4):
      next_x = x+dx[i]
      next_y = y+dy[i]
      if is_in_graph(next_x, next_y, n, m):
        if can_go(visit, graph,next_x, next_y):
          if (next_x, next_y) not in queue:
            queue.append((next_x, next_y))
            graph[next_x][next_y] = graph[x][y]

  return visit

n,m = map(int, input().split())
graph = []
start = None
for i in range(n):
  l = list(map(int, input().split()))
  for j in range(m):
    ground = l[j]
    if ground == 2:
      start = (i, j)
      l[j] = -1
  graph.append(l)

visit = BFS(start, graph, n, m)

for i in range(n):
  for j in range(m):
    if (i, j) in visit:
      print(graph[i][j], end="")
    else:
      if graph[i][j] == 1:
        print("-1", end="")
      else:
        print(graph[i][j], end="")
    if j == m-1:
      print()
    else:
      print(" ", end="")