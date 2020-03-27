while 1:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    if b > a and b % a == 0:
        print("factor")
    elif a > b and a % b == 0:
        print("multiple")
    else:
        print("neither")