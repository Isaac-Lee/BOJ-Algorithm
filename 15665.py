from itertools import product as P
n = list(map(int, input().split()))
numbers = list(map(int, input().split()))
numbers.sort()
comb = list(set(P(numbers, repeat=n[1])))
comb.sort()
for i in comb:
    answer = ""
    for j in i:
        answer += str(j) + " "
    print(answer)