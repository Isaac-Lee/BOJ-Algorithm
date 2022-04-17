from collections import deque
import sys
input = sys.stdin.readline

def dfs(s, g):
    visited = [False for _ in range(n+1)]
    depth = [-1 for _ in range(n+1)]
    stack = deque([[s, 0]])
    while stack:
        node, d = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        depth[node] = d
        for c in g[node]:
            if not visited[c]:
                stack.append([c, d+1])
    return depth

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

    depth = dfs(r, graph)
    for i in range(1, n+1):
        print(depth[i])