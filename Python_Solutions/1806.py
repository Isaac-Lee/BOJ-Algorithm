N, S = map(int, input().split())
arr = list(map(int, input().split()))

answer = N+1
curr_sum = 0
start = 0
end = 0

while end < N:
    while curr_sum < S and end < N:
        curr_sum += arr[end]
        end += 1
    while curr_sum >= S and start < N:
        if end - start < answer:
            answer = end - start
        curr_sum -= arr[start]
        start += 1

if answer > N: print(0)
else: print(answer)
