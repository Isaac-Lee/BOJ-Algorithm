E, S, M = map(int, input().split())
e = s = m = 1

for i in range(1, 7981):
    if (e, s, m) == (E, S, M):
        print(i)
        break
    e = e%15 + 1
    s = s%28 + 1
    m = m%19 + 1
