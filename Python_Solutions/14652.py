n, m, k = list(map(int, input().split()))
p = 0

for i in range(n):
    for j in range(m):
        if p == k:
            print(i, j)
            exit(0)
        else:
            p += 1