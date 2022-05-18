from collections import defaultdict, deque
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    B = defaultdict(list)
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    degree = [0 for _ in range(N + 1)]
    memo = [0 for _ in range(N + 1)]

    for k in range(K):
        X, Y = map(int, input().split())
        B[X].append(Y)
        degree[Y] += 1
    W = int(input())

    visit = set()
    queue = deque()
    for i in range(1, N+1):
        if degree[i] == 0:
            queue.append(i)
            memo[i] = D[i]

    while queue:
        b = queue.popleft()
        for i in B[b]:
            degree[i] -= 1
            memo[i] = max(memo[b]+D[i], memo[i])
            if degree[i] == 0:
                queue.append(i)

    print(memo[W])
