n, m = map(int, input().split())
a = []
b = []
result = []
for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))
for i in range(n):
    result.append([])
    for j in range(m):
        result[i].append(a[i][j] + b[i][j])
for i in range(n):
    print(*result[i])
