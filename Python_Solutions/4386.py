n = int(input())
star = []
edge = []
for i in range(n):
    x, y = map(float, input().split())
    star.append([x, y])
for i in range(n):
    for j in range(i+1, n):
        edge.append()