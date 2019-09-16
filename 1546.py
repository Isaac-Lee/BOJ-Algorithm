n = int(input())
nList = [int(k) for k in input().split()]
m = max(nList)
for i in range(0,n):
    nList[i] = nList[i] / m * 100
print(sum(nList))