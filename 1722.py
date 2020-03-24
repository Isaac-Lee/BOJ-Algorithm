from itertools import permutations
comb = list(permutations([k for k in range(1, int(input())+1)]))
p = list(map(int, input().split()))
if p[0] == 1:
    answer = ""
    for j in comb[p[1]]:
        answer += str(j) + " "
    print(answer)
else:
    case = tuple(map(int, input().split()))
    print(comb.index(case))