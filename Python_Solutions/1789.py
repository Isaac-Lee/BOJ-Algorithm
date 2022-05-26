s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    t = n * (n + 1) / 2
    n += 1
print(n - 1)