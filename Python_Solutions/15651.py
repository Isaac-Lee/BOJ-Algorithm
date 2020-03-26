# 반복문 사용불
from itertools import product
n = list(map(int, input().split()))
items = [k for k in range(1,n[0]+1)]
comb = list(product(items, repeat = n[1]))
for i in comb:
    answer = ""
    for j in i:
        answer += str(j)+" "
    print(answer)