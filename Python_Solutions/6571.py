d = [0 for i in range(1001)]
d[1] = 1
d[2] = 2
for i in range(3, 1001, 1):
    d[i] = d[i - 1] + d[i - 2]

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    count = 0
    for i in range(1, 1001, 1):
        if a <= d[i] <= b:
            count += 1
    print(count)