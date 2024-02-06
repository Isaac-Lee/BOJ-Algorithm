N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
  for j in range(1, i+1):
      dp[i] = max(dp[i], P[j] + dp[i-j])

print(dp[N])