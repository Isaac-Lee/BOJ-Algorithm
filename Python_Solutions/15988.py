import sys
input = sys.stdin.readline

dp = [0 for i in range(1000001)]
dp[0] = 1
dp[1] = 1
dp[2] = 2

n = int(input())
for i in range(3, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for i in range(n):
    k = int(input())
    print(dp[k]%1000000009)