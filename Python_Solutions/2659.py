from itertools import combinations

n = input().split()
target = []
target.append(n[:])
target.append(n[1:] + n[:1])
target.append(n[2:] + n[:2])
target.append(n[3:] + n[:3])

target = map(lambda x: int("".join(x)), target)
target = min(target)

num = [1, 1, 1, 1]
answer = 1
while int("".join(map(str, num))) < target:
    num[3] += 1
    if num[3] > 9:
        num[2] += 1
        num[3] = num[0] + 1
        if num[2] > 9:
            num[1] += 1
            num[2] = num[0]
            num[3] = num[1]
            if num[1] > 9:
                num[0] += 1
                num[3] = num[2] = num[1] = num[0]
    answer += 1
    print(*num)
print(answer)