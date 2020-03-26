import sys

n=int(sys.stdin.readline())
nlist = []
for i in range(1,n+1):
    nlist=[int(k) for k in sys.stdin.readline().split()]
    print('Case #%d:' % i, nlist[0]+nlist[1])