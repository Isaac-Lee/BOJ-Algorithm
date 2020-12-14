import heapq
import sys

def dijkstra(edge, V, src):
    INF = float('inf')
    distance = {}
    queue = []
    found = {}
    for n in range(V + 1):
        distance[n] = INF
        found[n] = False
    distance[src] = 0

    heapq.heappush(queue, [0, src])

    while queue:
        v = heapq.heappop(queue)
        found[v[1]] = True  # v[1]의 최단경로를 구함
        for node, weight in edge[v[1]]:
            if found[node]: continue
            if distance[node] > distance[v[1]] + weight:
                distance[node] = distance[v[1]] + weight
                heapq.heappush(queue, [distance[node], node])

    return distance


if __name__ == '__main__':
    V, E = map(int, input().split())
    src = int(input())
    edges = {}
    for i in range(V+1):
        edges[i] = []

    for _ in range(E):
        i, j, c = map(int, sys.stdin.readline().split())
        edges[i].append([j, c])

    for i in range(1, V+1):
        dist = dijkstra(edges, V, src)
        if dist[i] == float('inf'):
            print('INF')
        else:
            print(dist[i])