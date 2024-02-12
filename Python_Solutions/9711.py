import sys
def pibo(n):
    n1=0
    n2=1
    answer=0
    if n == 1:
        return n2
    else:
        for _ in range(2, n+1):
            answer = n1 + n2
            n1, n2 = n2, answer
        return answer
    

for i in range(1, int(sys.stdin.readline())+1):
    p, q = map(int, sys.stdin.readline().split())
    memo = [[0, 0]] * (p+1)
    print("Case #%d: %d" % (i, pibo(p)%q))