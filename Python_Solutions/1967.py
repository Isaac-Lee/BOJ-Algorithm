from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def dfs(s, t):
    visited = {s}
    stack = []
    result = [0, 0]
    for c in t[s]:
        stack.append([c, t[s][c]])
        if result[1] < t[s][c]:
            result = [c, t[s][c]]
    stack = deque(stack)
    while stack:
        node = stack.pop()
        c, v = node
        if c in visited:
            continue
        visited.add(c)
        if result[1] < v:
            result = node
        for child in t[c]:
            stack.append([child, v+t[c][child]])
    return result

n = int(input())
if n == 1:
    print(0)
    exit(0)

tree = {}
for i in range(1, n+1):
    tree[i] = {}

for i in range(n-1):
    p, c, v = map(int, input().split())
    tree[p][c] = v
    tree[c][p] = v

n1, d1 = dfs(1, tree)
n2, d2 = dfs(n1, tree)

# print(n1, d1)
# print(n2, d2)
print(d2)


