import sys

def makeBy(n):
    for i in range(3, n+1):
        memo[3] = memo[1] + memo[2]
        memo[1], memo[2] = memo[2], memo[3]
    print(memo[3]%15746)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    memo = [0,1,2,0]
    makeBy(n)