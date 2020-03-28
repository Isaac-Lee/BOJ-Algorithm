n = int(input())
b = 2
while True:
    if n == 1 or n == 2:
        print(n)
        break
    b *= 2
    if b >= n:
        print((n - (b // 2)) * 2)
        break