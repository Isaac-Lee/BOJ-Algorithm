import sys

def makeOne(n):
    for i in range(2, n+1):
        memo[i] = memo[i-1]
        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i//3])
        if i % 2 == 0:
            memo[i] = min(memo[i], memo[i//2])
        memo[i] += 1
    return memo[n]

# # 재귀로 해결한 코드 : 재귀재한 걸려서 실패
# def makeOne(n):
#     if memo[n] > 0:
#         return memo[n]
#
#     if n == 1:
#         return memo[n]
#
#     memo[n] = makeOne(n-1)
#     if n % 3 == 0:
#         memo[n] = min(memo[n], makeOne(n // 3))
#     if n % 2 == 0:
#         memo[n] = min(memo[n], makeOne(n // 2))
#
#     memo[n] += 1
#     return memo[n]

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    memo = [0] * (n + 1)
    print(makeOne(n))
