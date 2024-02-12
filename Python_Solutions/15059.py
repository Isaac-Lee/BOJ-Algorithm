a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0
for i in range(3):
    if a[i]<b[i]:
        answer += b[i]-a[i]
print(answer)