n = int(input())
nlist = [int(k) for k in input().split()]
nlist.sort()
print(nlist[0],nlist[n-1])