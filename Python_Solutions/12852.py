import sys

def makeOne(n):
    for i in range(2, n+1):
        memo[i][0] = memo[i-1][0] + 1
        memo[i][1] = memo[i-1][1] + [i]
        if i % 3 == 0 and memo[i][0] > memo[i//3][0]+1:
            memo[i][0] = memo[i//3][0] + 1
            memo[i][1] = memo[i//3][1] + [i]
        if i % 2 == 0 and memo[i][0] > memo[i//2][0]+1:
            memo[i][0] = memo[i//2][0] + 1
            memo[i][1] = memo[i//2][1] + [i]
    return


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    memo = [[0, []] for _ in range(n+1)]
    memo[1] = [0, [1]]
    makeOne(n)
    print(memo[n][0])
    print(*sorted(memo[n][1], reverse=True))