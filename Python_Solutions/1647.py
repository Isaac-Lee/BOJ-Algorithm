import time
import heapq as hq
import sys

parent = {}

def make_set(v):
    parent[v] = v

def find(v):
    if parent[v] == v: return v
    else:
        parent[v] = find(parent[v])
        return parent[v]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if root1 != root2:
        if root1 > root2:
            parent[root2] = root1
        else:
            parent[root1] = root2

def kruskal(e_list, n):
    for u in range(1, n+1):
        make_set(u)
        
    sum = 0
    a = n-2

    while e_list:
        e = hq.heappop(e_list)
        cost, u, v = e
        if find(u) != find(v):
            union(u, v)
            sum += cost
            a-=1
        if a <= 0:
          break

    return sum

if __name__ == '__main__':
    start = time.time()
    n, m = map(int, input().split())

    edge = []
    for _ in range(m):
        u, v, c = map(int, sys.stdin.readline().split())
        hq.heappush(edge, [c, u, v])

    print(kruskal(edge, n))
    print("time :", (time.time() - start)*10000)