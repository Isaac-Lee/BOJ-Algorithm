import sys

def pibo(n):
    if memo[n] > -1:
        return memo[n]

    if n == 0:
        memo[n] = 0
        return memo[n]

    if n == 1:
        memo[n] = 1
        return memo[n]
    else:
        memo[n] = pibo(n-1) + pibo(n-2)
        return memo[n]


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    memo = [-1] * (n + 1)
    print(pibo(n))