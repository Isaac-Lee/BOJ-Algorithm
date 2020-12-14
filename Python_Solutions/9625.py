n = int(input())
answer = [1, 0]
for _ in range(n):
    a, b = answer
    answer[0] = b
    answer[1] = a + b
print(*answer)
