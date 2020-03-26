import sys
n = []
for i in range(int(input())):
    n.append(int(sys.stdin.readline()))
n.sort(reverse=True)
for k in n:
    print(k)