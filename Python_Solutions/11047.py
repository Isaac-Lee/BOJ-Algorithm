n, k = map(int, input().split())
money = []
answer = 0
for i in range(n):
    money.append(int(input()))
money.sort(reverse=True)
for m in money:
    answer += k//m
    k = k%m
print(answer)