import sys
n = int(input())
d = 0
d_min = sys.maxsize
for _ in range(n):
    d += int(input())
    if d < 0 and d < d_min:
        d_min = d
if d_min == sys.maxsize:
    print(0)
else:
    print(-d_min)