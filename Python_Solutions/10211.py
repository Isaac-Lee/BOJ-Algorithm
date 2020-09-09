case = int(input())
for _ in range(case):
    n = int(input())
    arr = list(map(int, input().split()))
    memo = [i for i in range(n)]
    memo[0] = arr[0]
    for i in range(1, n):
        memo[i] = max(0, memo[i-1]) + arr[i]
    print(max(memo))