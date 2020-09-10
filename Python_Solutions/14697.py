import sys

A,B,C,N = map(int,sys.stdin.readline().split())
dp=[0]*301
dp[A], dp[B], dp[C] = 1, 1, 1

if N%A==0 or N%B==0 or N%C==0:
    print(1)
else:
    for i in range(2*A, N+1):
        if dp[i-A] or dp[i-B] or dp[i-C]:
            dp[i]=1
    print(dp[N])