def length(x1, x2, y1, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5


n = int(input())
for i in range(n):
    case = [int(k) for k in input().split()]
    x1 = case[0]
    y1 = case[1]
    r1 = case[2]
    x2 = case[3]
    y2 = case[4]
    r2 = case[5]
    if r1 > r2:
        c = r1
        r1 = r2
        r2 = c
    if (x1 == x2) and (y1 == y2) and (r1 == r2):
        print(-1)
    if (length(x1, x2, y1, y2) + r1) > r2:
        if length(x1, x2, y1, y2) > r1 + r2:
            print(0)
        elif length(x1, x2, y1, y2) == r1 + r2:
            print(1)
        else:
            print(2)
    elif (length(x1, x2, y1, y2) + r1) == r2:
        print(1)
    else:
        print(0)


# TODO 문제 틀렸음 다시 풀기