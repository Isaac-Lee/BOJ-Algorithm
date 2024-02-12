import sys
input = sys.stdin.readline

n, b = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(n)]
mod = 1000

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

for row in div(n, m, b):
    for num in row:
        print(num%mod, end=" ")
    print()