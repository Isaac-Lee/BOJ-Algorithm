import sys

def makeBy(n):
    dp1 = 1
    dp2 = 2
    answer = 0
    if (n == 1):
        return dp1
    if (n == 2):
        return dp2
    for i in range(3, n+1):
        answer = dp1 + dp2
        dp1, dp2 = dp2, answer
    return answer%15746

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(makeBy(n))