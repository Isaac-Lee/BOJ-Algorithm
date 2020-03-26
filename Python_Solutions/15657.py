from itertools import combinations_with_replacement as C
n = list(map(int, input().split()))
numbers = list(map(int, input().split()))
numbers.sort()
comb = list(C(numbers, n[1]))
comb.sort()
for i in comb:
    answer = ""
    for j in i:
        answer += str(j) + " "
    print(answer)