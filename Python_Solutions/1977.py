M = int(input())
N = int(input())
s = 0
m = 10001
for n in range(M, N+1):
    n_sq = n**0.5
    if n_sq == int(n_sq):
        s += n
        m = min(n, m)
if s != 0:
    print(s)
    print(m)
else:
    print(-1)