import sys, math

def init(node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start + end) // 2
        tree[node] = init(node*2,start,mid) + init(node*2+1,mid+1,end)
    return tree[node]

def get_sum(node,start,end,i,j):
    if i<start or i>end:
        return 0
    if i<=start and end<=j:
        return tree[node]
    mid = (start + end) // 2
    return get_sum(node*2,start,mid,i,j) + get_sum(node*2+1,mid+1,end,i,j)
           
def update(node,start,end,i,diff):
    if i<start or i>end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node*2, start, mid, i, diff)
        update(node*2+1, mid+1, end, i, diff)

n, m, k = map(int, input().split())

a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))

tree = [0]*(4*n)

init(1, 0, n-1)

for _ in range(m+k):
    t1, t2, t3 = map(int, sys.stdin.readline().split())
    if t1 == 1:
        diff = t3 - a[t2-1]
        a[t2-1] = t3
        update(1, 0, n-1, t2-1, diff)
    if t1 == 2:
        print(get_sum(1, 0, n-1, t2-1, t3-1))
