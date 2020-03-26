import sys

def padovan(n):
    if n < 6:
        return memo[n-1]
    for i in range(6, n+1):
        memo[5] = memo[0] + memo[4]
        del memo[0]
        memo.append(0)
    return memo[4]

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(sys.stdin.readline())
        memo = [1, 1, 1, 2, 2, 0]
        print(padovan(n))