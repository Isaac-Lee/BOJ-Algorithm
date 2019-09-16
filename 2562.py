nlist = []
for i in range(0,9):
    n = int(input())
    nlist.append(n)
MAX = 0
c=0
for i in range(0,9):
    if MAX < nlist[i]:
        MAX = nlist[i]
        c=i
print(MAX)
print(c+1)