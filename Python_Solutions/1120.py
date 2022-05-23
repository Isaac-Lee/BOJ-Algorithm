a, b = input().split()
if len(a) == len(b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    print(count)
else:
    dif = len(b) - len(a)
    min_count = len(b)
    for i in range(dif+1):
        count = 0
        for j in range(len(a)):
            if a[j] != b[i+j]:
                count += 1
        min_count = min(count, min_count)
    print(min_count)
