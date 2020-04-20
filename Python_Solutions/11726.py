n = int(input())

tmp1 = 1
tmp2 = 2
answer = 0

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for _ in range(3, n+1):
        answer = tmp1 + tmp2
        tmp1 = tmp2
        tmp2 = answer
    print(answer%10007)