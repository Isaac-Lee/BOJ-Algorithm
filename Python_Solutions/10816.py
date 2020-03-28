import sys
from collections import Counter

_ = sys.stdin.readline()
nums = sys.stdin.readline().split()
__ = sys.stdin.readline()
search = sys.stdin.readline().split()
answer = []
C = Counter(nums)
print(' '.join("%d" %C[m] if m in C else '0' for m in search))
