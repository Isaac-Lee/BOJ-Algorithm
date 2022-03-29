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
    for v in arr[1:]:
        if k[-1] < v:
            k.append(v)
        else:
            r = l_bound(k, 0, len(k), v)
            k[r] = v
    return k

n = int(input())
arr = list(map(int, input().split()))
print(len(lis(arr, n)))
