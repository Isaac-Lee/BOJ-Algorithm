N = int(input())
liquid = list(map(int, input().split()))

curr_min = 2000*1000*1000+1
curr_sum = 0
start = 0
end = N-1
answer_l = 0
answer_r = 0

while start < end:
    curr_sum = liquid[start] + liquid[end]
    if abs(curr_sum) < curr_min:
        answer_l = start
        answer_r = end
        curr_min = abs(curr_sum)
    if curr_sum > 0:
        end -= 1
    elif curr_sum < 0:
        start += 1
    else:
        break

print(liquid[answer_l], liquid[answer_r])
