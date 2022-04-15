from collections import deque
import sys
input = sys.stdin.readline

def dfs(s, g):
    visited = [False for _ in range(n+1)]
    index = [0 for _ in range(n+1)]
    stack = deque([s])
    count = 1
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        if index[node] == 0:
            index[node] = count
            count += 1
        for c in g[node]:
            if not visited[c]:
                stack.append(c)
    return index

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for i in range(1, n+1):
        graph[i] = []

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n+1):
        graph[i].sort()

    visit = dfs(r, graph)
    for i in range(1, n+1):
        print(visit[i])