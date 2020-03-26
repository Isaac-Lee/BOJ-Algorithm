n = int(input())
for i in range(n):
    case = [int(k) for k in input().split()]
    y = case[2]%case[0]*100
    x = case[2]//case[0]+1
    if case[2]%case[0] == 0:
        y=case[0]*100
        x-=1
    print(y+x)