for _ in range(int(input())):
    r, g, b = 0, 0, 0
    for i in range(10):
        dr, dg, db = map(int, input().split())
        r += dr; g += dg; b += db
    r /= 10; g /= 10; b /= 10
    print(int(r+0.5), int(g+0.5), int(b+0.5))