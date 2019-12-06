n = [int(k) for k in input().split()]
u = n[0]
d = n[1]
t = n[2]
l = 0
day=0
while(day*(u-d)+u < t):
    day+=1
print(day+1)