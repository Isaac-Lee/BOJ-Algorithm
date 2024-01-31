from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def can_go(x, y, n):
  if x < 0 or y < 0 or x >= n or y >= n:
    return False
  return True
    

def BFS(starts, graph, n):
  visit = set()
  ground = 0
  for start in starts:
    if start in visit:
      continue
    queue = deque()
    visit.add(start)
    queue.append(start)
    while queue:
      current = queue.popleft()
      x ,y = current
      for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]
        if can_go(new_x, new_y, n):
          if (new_x, new_y) in visit:
            continue
          if graph[new_x][new_y] != 0:
            visit.add((new_x, new_y))
            queue.append((new_x, new_y))
    ground += 1
  return ground
      

n = int(input())
graph = []
max_h = 0
min_h = 101
max_g = 1

for i in range(n):
  l = list(map(int, input().split()))
  max_h = max(max_h, max(l))
  min_h = min(min_h, min(l))
  graph.append(l)
  
for h in range(min_h, max_h):
  starts = []
  new_graph = []
  for i in range(n):
    l = []
    for j in range(n):
      current = graph[i][j]
      if current <= h:
        l.append(0)
      else:
        starts.append((i, j))
        l.append(current)
    new_graph.append(l)
  max_g = max(max_g, BFS(starts, new_graph, n))
  
print(max_g)