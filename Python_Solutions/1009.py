import sys
n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        print(1)
        continue
    if a%10 == 0:
        print(10)
        continue
    answer = 1
    for i in range(1, b):
        answer = (answer*a)%10
    print((answer*a)%10)
