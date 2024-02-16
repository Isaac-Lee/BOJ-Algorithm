from collections import deque

def bfs(f, s, g, u, d):
  visit = set()
  queue = deque()
  visit.add(s)
  queue.append((s, 0))
  while queue:
    c, count = queue.popleft()
    if c == g:
      return count
    cu = c+u
    cd = c-d    
    if cu <= f and cu not in visit:
      visit.add(cu)
      queue.append((cu, count+1))
    if cd > 0 and cd not in visit:
      visit.add(cd)
      queue.append((cd, count+1))
  return "use the stairs"

F, S, G, U, D = map(int, input().split())
print(bfs(F, S, G, U, D))
