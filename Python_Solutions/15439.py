from itertools import combinations
comb = list(combinations([i for i in range(int(input()))], 2))
print(len(comb)*2)