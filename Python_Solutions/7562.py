from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def can_go(x, y, l):
  if x < 0 or y < 0 or x >= l or y >= l:
    return False
  return True

def bfs(sx, sy, tx, ty, l):
  visit = set()
  queue = deque()
  queue.append((sx, sy, 0))
  visit.add((sx, sy))
  while queue:
    current = queue.popleft()
    cx, cy, n = current
    if (cx, cy) == (tx, ty):
      return n
    for i in range(8):
      nx = cx + dx[i]
      ny = cy + dy[i]
      if can_go(nx, ny, l):
        if (nx, ny) not in visit:
          queue.append((nx, ny, n+1))
          visit.add((nx, ny))
  return 0

for _ in range(int(input())):
  l = int(input())
  sx, sy = map(int, input().split())
  tx, ty = map(int, input().split())
  print(bfs(sx, sy, tx, ty, l))