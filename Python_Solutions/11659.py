import sys

n, t = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum = [0 for i in range(n)]
for i in range(n):
    if i == 0:
        sum[0] = arr[0]
        continue
    else:
        sum[i] = sum[i-1] + arr[i]
for _ in range(t):
    i, k = map(int, sys.stdin.readline().split())
    if i > k:
        temp = i
        i = k
        k = temp
    if i == 1:
        print(sum[k-1])
    else:
        print(sum[k-1]-sum[i-2])