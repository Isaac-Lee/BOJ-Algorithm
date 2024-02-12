import sys
input = sys.stdin.readline

n = int(input())
INF = sys.maxsize
price = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
    price[i][i] = 0

for _ in range(int(input())):
    s, d, v = map(int, input().split())
    price[s-1][d-1] = min(price[s-1][d-1], v)

for i in range(n):
    for x in range(n):
        if x == i:
            continue
        for y in range(n):
            if y == i:
                continue
            price[x][y] = min(price[x][y], price[x][i]+price[i][y])

for r in price:
    for p in r:
        if p == INF:
            print(0, end=" ")
        else:
            print(p, end=" ")
    print()

