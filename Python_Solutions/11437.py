from math import log2
from collections import deque

def generate_tree(tree, N):  # 양방향 그래프를 만든다
    for _ in range(N-1):
        parent, child = map(int, input().split())
        tree[child].append(parent)
        tree[parent].append(child)


def dfs(tree, parent_list, depth, N):  # depth 와 조상 노드를 구해서 넣어주기
    visited = [False for _ in range(N+1)]
    q = deque()
    q.append(1)

    while q:
        p = q.popleft()
        visited[p] = True
        for i in tree[p]:
            if not visited[i]:
                q.append(i)
                parent_list[i] = p
                depth[i] = depth[p] + 1


def compute_exp_parent(exp_parent, N):
    logN = int(log2(N) + 1)
    for i in range(1, N+1):
        for j in range(1, logN):
            exp_parent[i][j] = exp_parent[exp_parent[i][j-1]][j-1]


def search_lca(exp_parent, depth, N, M):
    logN = int(log2(N) + 1)
    for _ in range(M):
        a, b = map(int, input().split())

        if a == b:
            print(a)
            continue

        if depth[a] > depth[b]:
            a, b = b, a
        level_diff = depth[b] - depth[a]
        for i in range(logN):
            if level_diff & (1 << i):  # 1부터 1씩 비트 쉬프트 해서 이동
                b = exp_parent[b][i]

        for i in range(logN - 1, -1, -1):
            if exp_parent[a][i] != exp_parent[b][i]:
                a = exp_parent[a][i]
                b = exp_parent[b][i]
        print(exp_parent[b][0])


if __name__ == '__main__':
    N = int(input())
    tree = [[] for _ in range(N+1)]
    generate_tree(tree, N)

    depth = [0 for _ in range(N+1)]
    parent_list = [0 for _ in range(N+1)]
    dfs(tree, parent_list, depth, N)

    logN = int(log2(N) + 1)
    exp_parent = [[0 for _ in range(logN)] for i in range(N+1)]
    for i in range(N+1):
        exp_parent[i][0] = parent_list[i]
    compute_exp_parent(exp_parent, N)

    M = int(input())
    search_lca(exp_parent, depth, N, M)