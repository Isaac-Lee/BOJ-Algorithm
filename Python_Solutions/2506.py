n = int(input())
answer = 0
prev = 0
for a in input().split():
    if a == '1':
        answer += 1 + 1*prev
        prev += 1
    if a == '0':
        prev = 0
print(answer)
