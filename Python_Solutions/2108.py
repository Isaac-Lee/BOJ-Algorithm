import collections
import sys
N = int(sys.stdin.readline())
n = []

for i in range(N):
    t = int(sys.stdin.readline())
    n.append(t)
n.sort()
print(round(sum(n)/N))
print(n[N//2])
n_c = collections.Counter(n)
freq = n_c.most_common()
if N > 1:
    if freq[0][1] == freq[1][1]:
        print(freq[1][0])
    else:
        print(freq[0][0])
else:
    print(freq[0][0])
print(max(n)-min(n))