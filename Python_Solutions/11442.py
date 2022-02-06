import sys
input = sys.stdin.readline

n, b = 2, int(input())
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

if b%2 == 1:
    b += 1

print(div(n, m, b)[0][1])
