import sys

dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
for i in range(3, 1000001):
    dp[i] = dp[i-1]%15746 + dp[i-2]%15746

n = int(sys.stdin.readline())
print(dp[n]%15746)