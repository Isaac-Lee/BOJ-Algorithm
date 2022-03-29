def l_bound(arr, l, r, key):
    while l < r:
        m = (l+r)//2
        if arr[m] < key:
            l = m+1
        else:
            r = m
    return r

def lis(arr, l):
    k = [arr[0]]
    index = [-1] * l
    index[0] = 0
    for i in range(1, l):
        if k[-1] < arr[i]:
            k.append(arr[i])
            index[i] = len(k)-1
        else:
            r = l_bound(k, 0, len(k), arr[i])
            k[r] = arr[i]
            index[i] = r
    ci = len(k)-1
    result = []
    for i in range(l-1, -1, -1):
        if index[i] == ci:
            result.append(arr[i])
            ci -= 1
    return sorted(result)

n = int(input())
arr = list(map(int, input().split()))
LIS = lis(arr, n)
print(len(LIS))
print(*LIS)
