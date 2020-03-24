from itertools import permutations
for n in list(permutations([k for k in range(1, int(input())+1)])):
    answer = ""
    for j in n:
        answer += str(j) + " "
    print(answer)