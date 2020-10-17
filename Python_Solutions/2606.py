from collections import deque
n = int(input())
v = int(input())
graph = {}
for i in range(1, n+1):
    graph[i] = []
for _ in range(v):
    vertex = list(map(int, input().split()))
    a = vertex[0]
    b = vertex[1]
    graph[a].append(b)
    graph[b].append(a)

visit = set()
stack = deque()
stack.append(1)
while stack:
    c = stack.pop()
    if c not in visit:
        visit.add(c)
        stack.extend(graph[c])
print(len(visit)-1)