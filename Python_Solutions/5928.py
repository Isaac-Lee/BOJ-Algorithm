d, h, m = map(int, input().split())
t1 = d*24*60 + h*60 + m
t2 = 11*24*60 + 11*60 + 11
time = t1 - t2
if time < 0:
    print(-1)
else:
    print(time)