import sys

n=int(sys.stdin.readline())
for i in range(0,n):
    print(' '*(n-i-1)+'*'*(i+1))