import sys

n=int(sys.stdin.readline())
for i in range(0,n):
    print('*'*(i+1)+' '*(2*(n-i-1))+'*'*(i+1))
for i in range(1,n):
    print('*'*(n-i)+' '*(2*i)+'*'*(n-i))