# 반복문 사용불
from itertools import permutations
n = list(map(int, input().split()))
items = [k for k in range(1,n[0]+1)]
comb = list(permutations(items, n[1]))
for i in comb:
    answer = ""
    for j in i:
        answer += str(j)+" "
    print(answer)