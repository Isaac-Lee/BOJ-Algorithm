from itertools import combinations
h = [int(input()) for _ in range(9)]
for c in combinations(h, 7):
    if sum(c) == 100:
        for i in sorted(c):
            print(i)
        break
