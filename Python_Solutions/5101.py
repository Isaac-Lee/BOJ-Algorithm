while True:
    i, d, j = map(int, input().split())
    if i == d == j == 0:
        break
    if (j-i)%d == 0 and (j-i)//d+1 > 0:
        print((j-i)//d + 1)
    else:
        print('X')