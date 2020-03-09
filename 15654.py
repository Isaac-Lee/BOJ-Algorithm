from itertools import permutations as P
n = list(map(int, input().split()))
numbers = list(map(int, input().split()))
comb = list(P(numbers, n[1]))
comb.sort()
for i in comb:
    answer = ""
    for j in i:
        answer += str(j) + " "
    print(answer)