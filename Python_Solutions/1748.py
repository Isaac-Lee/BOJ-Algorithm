n = int(input())
m = 1
p = 1
count = 9
answer = 0
while n > 0:
    if m == 1:
        answer += p*(min(n, 9))
        n -= min(n, 9)
    else:
        answer += p * (min(n, m*9))
        n -= min(n, m*9)
        count = m*9
    m *= 10
    p += 1
print(answer)
