import sys

def pibo(n):
    if sum(memo[n]) > 0:
        return memo[n]

    if n == 0:
        memo[n] = [1, 0]
        return memo[n]
    if n == 1:
        memo[n] = [0, 1]
        return memo[n]
    if n == 2:
        memo[n] = [1, 1]
        return memo[n]
    else:
        memo[n] = [pibo(n-1)[0] + pibo(n-2)[0], pibo(n-1)[1] + pibo(n-2)[1]]
        return memo[n]


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    for i in range(n):
        k = int(sys.stdin.readline())
        memo = [[0, 0]] * (k+1)
        case = pibo(k)
        print(case[0], case[1])