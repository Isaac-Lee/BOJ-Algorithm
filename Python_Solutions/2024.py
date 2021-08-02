import sys, math

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        tree[node] = init(a,tree,node*2,start,(start+end)//2) + \
                       init(a,tree,node*2+1,(start+end)//2+1,end)
    return tree[node]

def sum(tree,node,start,end,i,j):
    if i>end or j<start:
        return 0
    if i<=start and end<=j:
        return tree[node]

    return sum(tree,node*2,start,(start+end)//2,i,j) \
           + sum(tree,node*2+1,(start+end)//2+1,end,i,j)
           
def update(tree,node,start,end,i,diff):
    if i>end or i<start:
        return -1
    tree[node] = tree[node] + diff
    if start != end:
        update(tree,node*2, start, (start+end)/2, i, diff)
        update(tree,node*2+1, (start+end)/2+1, end, i, diff)

n, m, k = map(int, input().split())

a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))

tree_list = [0]*(1 << (math.ceil(math.log(n,2))+1))

init(a, tree_list, 1, 0, n-1)

for _ in range(m+k):
    t1, t2, t3 = map(int, sys.stdin.readline().split())
    if t1 == 1:
        diff = t3 - a[t2-1]
        a[t2-1] = t3
        update(tree_list, 1, 0, n-1, t2-1, diff)
    if t1 == 2:
        print(sum(tree_list, 1, 0, n-1, t2-1, t3-1))
