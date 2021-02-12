from collections import deque


def dfs(x, y, n):
    stack = deque()
    stack.append([x, y])
    color = graph[x][y]
    while stack:
        cor = stack.pop()
        x = cor[0]
        y = cor[1]
        if graph[x][y] != color:
            continue
        if visited[x][y] == 0:
            visited[x][y] = 1
            if x - 1 >= 0:
                stack.append([x - 1, y])
            if x + 1 < n:
                stack.append([x + 1, y])
            if y - 1 >= 0:
                stack.append([x, y - 1])
            if y + 1 < n:
                stack.append([x, y + 1])


graph = []
n = int(input())
for _ in range(n):
    graph.append([c for c in input()])
answer_normal = 0
answer_weak = 0

visited = [[0 for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        if visited[x][y] == 0:
            dfs(x, y, n)
            answer_normal += 1

visited = [[0 for _ in range(n)] for _ in range(n)]
for x in range(n):
    for y in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
for x in range(n):
    for y in range(n):
        if visited[x][y] == 0:
            dfs(x, y, n)
            answer_weak += 1

print(answer_normal, answer_weak)