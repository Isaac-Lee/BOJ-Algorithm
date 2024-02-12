n = int(input())
x0, y0 = map(int, input().split())
px, py = map(int, input().split())
px, py = px-x0, py-y0
s = 0
for _ in range(2, n):
    x, y = map(int, input().split())
    vx, vy = x-x0, y-y0
    s += (vx*py - vy*px)/2
    px, py = vx, vy
print(round(abs(s), 1))