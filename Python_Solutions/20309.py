N = int(input())
nums = list(map(int, input().split()))

can = True
for i in range(N):
    if i%2 == 0:
        if nums[i]%2 == 0:
            can = False
            break
    else:
        if nums[i]%2 != 0:
            can = False
            break

if can:
    print("YES")
else:
    print("NO")