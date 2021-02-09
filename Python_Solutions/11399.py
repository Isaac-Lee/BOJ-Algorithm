n = int(input())
p = list(map(int, input().split()))
p.sort()
answer = 0
for i in range(n):
    answer += sum(p[:i+1])
print(answer)