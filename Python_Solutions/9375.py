from collections import defaultdict

t = int(input())
for _ in range(t):
    gadget = defaultdict(int)
    n = int(input())
    answer = 1
    for _ in range(n):
        name, type_ = input().split()
        gadget[type_] += 1
    for i in gadget.values():
        answer *= i+1
    print(answer - 1)