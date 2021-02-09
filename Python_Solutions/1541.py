num = input().split('-')
for i in range(len(num)):
    s = 0
    nums = num[i].split('+')
    for n in nums:
        s += int(n)
    num[i] = s

answer = num[0]
for i in range(1, len(num)):
    answer -= num[i]
print(answer)