from math import ceil
k,w,m = map(int, input().split())
if k > w:
    print(0)
else:
    print(ceil((w-k)/m))