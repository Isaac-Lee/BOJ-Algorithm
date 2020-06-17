n = int(input())
arr = {}
for i in range(n):
    a = int(input())
    if a in arr:
        arr[a] += 1
    else:
        arr[a] = 1

print(max(arr.values()))
print(arr)