n, k = map(int, input().split())
num = [x for x in range(2, n+1)]
count = 0
while num:
    p = num.pop(0)
    count += 1
    if count == k:
        print(p)
    nums = num.copy()
    for i in nums:
        if i%p == 0:
            num.remove(i)
            count += 1
            if count == k:
                print(i)