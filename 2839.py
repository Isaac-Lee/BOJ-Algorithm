N = int(input())
if N == 4 or N == 7:
    print(-1)
else:
    a = N % 5
    b = a % 3
    y = (b * 5 + a) // 3
    x = N // 5 - b
    print(int(x + y))
