while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    price = m//n
    total = 0
    for b in map(int, input().split()):
        if b > price:
            total += price
        else:
            total += b
    print(total)
