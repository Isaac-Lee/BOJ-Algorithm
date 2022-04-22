from collections import defaultdict, deque

def bfs_leaf_node(t):
    result=set()
    visited = set()
    q = deque()
    q.append(-1)
    while q:
        node = q.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node not in t or len(t[node]) == 0:
            result.add(node)
        else:
            for child in t[node]:
                q.append(child)
    return result

def bfs_del_node(t, s):
    q = deque()
    q.append(s)
    while q:
        node = q.popleft()
        for child in t[node]:
            q.append(child)
        t.pop(node)

def bfs_del_node_parent(t, d):
    q = deque()
    q.append(-1)
    while q:
        node = q.popleft()
        for child in t[node]:
            if child == d:
                t[node].remove(child)
                return
            q.append(child)

n=int(input())
parent=list(map(int, input().split()))
tree=defaultdict(list)
for i in range(n):
    tree[parent[i]].append(i)

d_node = int(input())
bfs_del_node(tree, d_node)
bfs_del_node_parent(tree, d_node)

leaf_n = bfs_leaf_node(tree)
if -1 in leaf_n:
    leaf_n.remove(-1)

print(len(leaf_n))
