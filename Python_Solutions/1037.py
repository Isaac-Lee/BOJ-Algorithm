i = int(input())
n = list(map(int, input().split()))
n.sort()
if len(n) == 1:
    print(n[0]**2)
else:
    print(n[0]*n[i-1])