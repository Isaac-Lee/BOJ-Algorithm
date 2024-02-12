import sys

input = sys.stdin.readline
N, K = map(int, input().split())
bag = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(K + 1)]

for i in range(N):
    for j in range(K, 0, -1):
        if bag[i][0] <= j:
            dp[j] = max(dp[j], dp[j - bag[i][0]] + bag[i][1])

print(dp[-1])