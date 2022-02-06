import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
s = [[] for _ in range(V+1)]
d = [INF] * (V+1)
heap = []

def dijkstra(src):
    d[src] = 0
    heapq.heappush(heap, [0, src])

    while heap:
        w, n = heapq.heappop(heap)
        for node, weight in s[n]:
            new_weight = weight + w
            if new_weight < d[node]:
                d[node] = new_weight
                heapq.heappush(heap, [new_weight, node])

for _ in range(E):
    i, j, c = map(int, input().split())
    s[i].append([j, c])

dijkstra(K)

for i in range(1, V + 1):
    if d[i] == INF:
        print('INF')
    else:
        print(d[i])
