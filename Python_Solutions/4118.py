import sys
input = sys.stdin.readline
T = int(input())
while T > 0:
    s = set()
    for _ in range(T):
        for c in input().split():
            s.add(int(c))
    if set(range(1,50)) <= s:
        print('Yes')
    else:
        print('No')
    T = int(input())