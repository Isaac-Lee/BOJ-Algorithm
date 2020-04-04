def pinaryNumber(n):
    answer = 1
    dp1 = 1
    dp2 = 2
    if n == 1:
        return dp1
    if n == 2:
        return dp1
    if n == 3:
        answer = dp1 + dp2
        dp1 = dp2
        dp2 = answer
        return dp1
    for i in range(4, n+1):
        answer = dp2 + dp1
        dp1 = dp2
        dp2 = answer
    return answer

if __name__ == '__main__':
    n = int(input())
    print(pinaryNumber(n))