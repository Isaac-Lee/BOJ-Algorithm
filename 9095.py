import sys


def make123(n):

    if memo[n] > 0:
        return memo[n]

    if n == 1 or n == 0:
        memo[n] = 1
        return memo[n]

    memo[n] += make123(n-1)
    if n-3 >= 0:
        memo[n] += make123(n-3)
    if n-2 >= 0:
        memo[n] += make123(n-2)
    return memo[n]


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for _ in range(n):
        k = int(sys.stdin.readline())
        memo = [0] * (k + 1)
        print(make123(k))