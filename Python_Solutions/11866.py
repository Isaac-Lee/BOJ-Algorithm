N, K = map(int, input().split())
people = list(range(1, N+1))
result = []
i = K-1
while True:
    result.append(people.pop(i))
    if not people:
        break
    i = (i+K-1) % len(people)
print('<'+', '.join(map(str, result))+'>')