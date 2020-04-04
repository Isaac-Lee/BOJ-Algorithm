n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))
dp = [0, w[1]]
if n > 1:
    dp.append(w[1] + w[2])
for i in range(3, n+1):
    dp.append(max(dp[i - 2] + w[i], dp[i - 3] + w[i] + w[i-1]))
print(dp[n])