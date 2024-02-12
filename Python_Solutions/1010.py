from functools import reduce

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print(1)
    elif a == 1:
        print(b)
    else:
        a = max(b - a, a)
        upper = [i for i in range(a+1, b+1)]
        down = [i for i in range(1, b-a+1)]
        print(reduce(lambda x, y: x * y, upper) // reduce(lambda x, y: x * y, down))