n, t = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(t):
    i, k = map(int, input().split())
    print(sum(arr[i-1:k]))