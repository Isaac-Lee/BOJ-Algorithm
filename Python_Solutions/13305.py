N = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))
min_p = p[0]
answer = 0
for i in range(0, N-1):
    min_p = min(min_p, p[i])
    answer += min_p*d[i]
print(answer)
