dp = [0 for _ in range(1001)]
dp[1] = -1
dp[2] = 1
dp[3] = -1
dp[4] = -1

for i in range(5, 1001):
    if dp[i-1]>0 or dp[i-3]>0 or dp[i-4]>0:
        dp[i] = -1
    else:
        dp[i] = 1


n = int(input())
print("SK" if dp[n]==-1 else "CY")
