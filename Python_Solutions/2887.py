import sys

parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    root1 = find(u)
    root2 = find(v)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(v_list, e_list):
    for u in v_list:
        make_set(u)

    edges = e_list
    edges.sort()
    mst = []
    sum = 0

    for e in edges:
        cost, u, v = e
        if find(u) != find(v):
            union(u, v)
            mst.append(e)
            sum += cost

    return sum

if __name__ == '__main__':
  n = int(input())

  node = []

  for i in range(1, n+1):
    x, y, z = map(int, sys.stdin.readline().split())
    node.append((x, y, z, i))
  
  edge = []
  for j in range(3):
    node.sort(key=lambda x:x[j])
    before_location = node[0]
    for i in range(1, n):
      cur_location = node[i]
      edge.append([abs(node[i][j]-node[i-1][j]), before_location, cur_location])
      before_location = cur_location
  
  print(kruskal(node, edge))