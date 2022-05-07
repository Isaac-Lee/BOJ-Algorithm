s = 0
a,b = map(int, input().split())

n = 1
count = 0
while n:
    for _ in range(n):
        count += 1
        if a <= count <= b:
            s += n
    if count > b:
        break
    n += 1
print(s)