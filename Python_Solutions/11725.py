import sys
from collections import deque

def bfs(t):
    visit = [-1 for _ in range(n+1)]
    parent = [-1 for _ in range(n+1)]
    queue = deque([1])

    while queue:
        node = queue.popleft()
        if visit[node] > 0:
            continue
        visit[node] = 1
        for child in t[node]:
            if parent[child] < 0:
                parent[child] = node
            queue.append(child)
    return parent

input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n-1):
    i, j = map(int, input().split())
    if i not in tree:
        tree[i] = [j]
    else:
        tree[i].append(j)
    if j not in tree:
        tree[j] = [i]
    else:
        tree[j].append(i)
for parent in bfs(tree)[2:]:
    print(parent)