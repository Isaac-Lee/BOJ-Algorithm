import sys

n=int(sys.stdin.readline())
nlist = []
for i in range(0,n):

    nlist=[int(k) for k in sys.stdin.readline().split()]
    print(nlist[0]+nlist[1])