n = int(input())
n1=0
n2=1
answer=0
if n == 1:
    print(n2)
else:
    for i in range(2, n+1):
        answer = n1 + n2
        n1, n2 = n2, answer
    print(answer)