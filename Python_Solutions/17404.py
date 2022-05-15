import sys
input = sys.stdin.readline

N = int(input())
house_price = [list(map(int, input().split())) for _ in range(N)]
INF = sys.maxsize
answer = INF

for c in range(3):
    house = [INF, INF, INF]
    house[c] = house_price[0][c]
    for i in range(1, N):
        price = house_price[i]
        new_price = [0, 0, 0]
        for k in range(3):
            new_price[k] = min(house[:k]+house[k+1:]) + price[k]
        house = new_price
    answer = min(answer, min(house[(c+1)%3], house[(c+2)%3]))

print(answer)
