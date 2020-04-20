n = int(input())

tmp = 1
answer = 0

if n == 1:
    print(1)
else:
    for i in range(2, n+1):
        if i%2 == 0:
            answer = tmp*2 + 1
        else:
            answer = tmp*2 - 1
        tmp = answer
    print(answer%10007)
