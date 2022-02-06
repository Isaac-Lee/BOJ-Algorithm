import sys
input = sys.stdin.readline

n = 2
m = [[1, 1], [1, 0]]
mod = 1000000007

def product(s, m1, m2):
    answer = [[0 for _ in range(s)] for _ in range(s)]
    for i in range(s):
        for j in range(s):
            for k in range(s):
                answer[i][j] += m1[i][k] * m2[k][j]
            answer[i][j] %= mod
    return answer

def div(s, m, n):
    if n == 1:
        return m
    elif n == 2:
        return product(s, m, m)
    else:
        tmp = div(s, m, n//2)
        if n%2 == 0:
            return product(s, tmp, tmp)
        else:
            return product(s, product(s, tmp, tmp), m)

def gcd(a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

b1, b2 = map(int, input().split())

print(div(n, m, gcd(b1, b2))[0][1])
# print(gcd(div(n, m, b1)[0][1], div(n, m, b2)[0][1])%mod)