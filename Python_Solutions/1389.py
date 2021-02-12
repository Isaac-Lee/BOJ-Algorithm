from collections import deque

def bfs(x):
    q.append(x)
    dist = [-1 for _ in range(n)]
    dist[x] = 0
    while q:
        x = q.popleft()
        for i in graph[x]:
            if dist[i] == -1:
                dist[i] = dist[x] + 1
                q.append(i)
    cnt = 0
    for i in range(n):
        if dist[i] != -1:
            cnt += dist[i]
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
q, res, ans = deque(), [], []

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    graph[x].append(y)
    graph[y].append(x)

for i in range(n):
    res.append(bfs(i))

for i in range(n):
    if res[i] == min(res):
        ans.append(i)
print(min(ans)+1)