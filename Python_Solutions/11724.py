import sys
from collections import deque

n, m = map(int, input().split())
graph = {}
visit = set()
CC = 0
for i in range(1, n+1):
    graph[i] = []
for _ in range(m):
    node = sys.stdin.readline().split()
    x = int(node[0])
    y = int(node[1])
    graph[x].append(y)
    graph[y].append(x)
for i in range(1, n+1):
    if i not in visit:
        stack = deque([i])
        while stack:
            num = stack.pop()
            if num not in visit:
                visit.add(num)
                stack.extend(graph[num])
        CC += 1
print(CC)