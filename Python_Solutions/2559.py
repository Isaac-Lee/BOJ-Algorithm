n, t = map(int, input().split())
arr = list(map(int, input().split()))
temp = sum(arr[0:t])
answer = temp
for i in range(1, n-t+1):
    temp = temp + arr[i+t-1] - arr[i-1]
    if answer < temp:
        answer = temp
print(answer)