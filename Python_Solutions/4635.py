while True:
    n = int(input())
    total = 0
    p = 0
    if n == -1:
        break
    for _ in range(n):
        s, t = map(int,input().split())
        total += s*(t-p)
        p = t
    print(total, 'miles')