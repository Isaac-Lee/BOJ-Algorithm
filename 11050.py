# def binoCoef(n, k):
#     for i in range(n+1):
#         memo[i][0] = 1
#     for i in range(k+1):
#         memo[i][i] = 1
#
#     for i in range(1, n + 1):
#         for j in range(1, k + 1):
#             if i == j:
#                 pass
#             memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
#
#     return memo[n][k]
import math


def binoCoef(n, k):
    nFac = math.factorial(n)
    kFac = math.factorial(k)
    return nFac//(kFac*math.factorial(n-k))

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    # memo = [[0]*(k+1)]*(n+1)
    print(binoCoef(n, k))