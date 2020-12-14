# 왜 안되는지 모르겠는 코드
# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# w = []
# v = []
# for _ in range(n):
#     weight, value = map(int, sys.stdin.readline().split())
#     w.append(weight)
#     v.append(value)
#
# knap = [[0] * k+1 for _ in range(n + 1)]
# for i in range(n+1):
#     for j in range(k+1):
#         if i == 0 or j == 0:
#             knap[i][j] = 0
#         elif w[i-1] <= j:
#             knap[i][j] = max(v[i - 1] + knap[i - 1][j - w[i - 1]], knap[i - 1][j])
#         else:
#             knap[i][j] = knap[i - 1][j]
# print(knap[n][k])


# import sys
#
# r = sys.stdin.readline
# N, W = map(int, r().split())
# bag = [tuple(map(int, r().split())) for _ in range(N)]
#
# knap = [0 for _ in range(W+1)]
#
# for i in range(N):
#     for j in range(W, 1, -1):
#         if bag[i][0] <= j:
#             knap[j] = max(knap[j], knap[j-bag[i][0]] + bag[i][1])
#
# print(knap[-1])