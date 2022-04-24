s=0
m=100
for _ in range(7):
    x = int(input())
    if x%2==0:
        continue
    s+=x
    m=min(m,x)
if s == 0:
    print(-1)
else:
    print(s)
    print(m)