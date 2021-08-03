n = int(input())
if n == 1:
    print(4)
elif n == 2:
    print(6)
else:
    a = [1, 1, 6]
    for _ in range(n-2):
        temp = a[1]
        a[1] = a[0] + a[1]
        a[0] = temp
        a[2] += a[1]*2
    print(a[2])