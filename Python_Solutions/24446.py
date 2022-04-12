from collections import deque
import sys
input = sys.stdin.readline

def BFS(G, N, R):
    visited = set()
    visit = [-1] * (N+1)
    queue = deque([[R, 0]])
    while queue:
        n, d = queue.popleft()
        if n in visited:
            continue
        visited.add(n)
        visit[n] = d
        for v in sorted(G[n]):
            queue.append([v, d+1])
    return visit[1:]


if __name__ == '__main__':
    n, m, r = map(int, input().split())
    graph = {}
    for i in range(n):
        graph[i+1] = []
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for k in BFS(graph, n, r):
        print(k)