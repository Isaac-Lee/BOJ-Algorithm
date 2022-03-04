bee = list(map(int, input().split()))
n = sum(bee)//3
i = 0
for b in bee:
    if b>=n:
        break
    i+=1
if i == 1:
    print((bee[1]-n)+(bee[2]-n)*2)
elif i == 2:
    print((n-bee[0])*2+(n-bee[1]))
else:
    print(0)