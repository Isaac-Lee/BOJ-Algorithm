import sys
n = int(input())
s = list(map(int, input().split()))
inter = sys.maxsize
for i in range(1, n):
    inter = min(inter, abs(s[i]-s[i-1]))
print(inter)
