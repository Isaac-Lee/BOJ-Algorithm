t = int(input())
for i in range(t):
    f = int(input())
    n = int(input())
    for j in range(f):
        n = n*(n+1)//2
    print(n)