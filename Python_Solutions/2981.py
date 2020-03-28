n = []
answer = []
for i in range(int(input())):
    n.append(int(input()))
for k in range(max(n)):
    c = list(map(lambda x: x%i, n))
    if c.count(c[0]) == n:
        answer.append(i)
for i in range(len(answer)):
    print(answer[i], end=' ')
