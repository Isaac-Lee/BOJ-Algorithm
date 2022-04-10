from collections import deque
import sys
input = sys.stdin.readline

def BFS(G, N, R):
    visited = set()
    visit_count = 0
    visit = [0] * (N+1)
    queue = deque([R])
    while queue:
        n = queue.popleft()
        if n in visited:
            continue
        visited.add(n)
        visit_count += 1
        visit[n] = visit_count
        for v in sorted(G[n]):
            queue.append(v)
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