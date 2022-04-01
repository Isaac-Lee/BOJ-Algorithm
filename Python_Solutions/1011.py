for i in range(int(input())):
    x, y = map(int, input().split())
    d = y-x
    v = 0
    m = 1
    c = 0
    while v < d:
        c += 1
        v += m
        if c%2 == 0:
            m += 1
    print(c)