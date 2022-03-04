n, m = map(int, input().split())
num = []
for _ in range(n):
    num.append(int(input()))
for _ in range(m):
    i, j = map(int, input().split())
    l = num[i-1:j]
    print(min(l), max(l))
