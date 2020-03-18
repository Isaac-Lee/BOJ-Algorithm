# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]
numbers = list(map(int, input().split()))
m = numbers.index(min(numbers))
if m >= k:
    back = len(numbers[m+1:])
    over = back%(k-1)-1
    answer = ((len(numbers[:m])-over)//(k-1) + (back+over)//(k-1))
    if (len(numbers[:m])-over)%(k-1) > 0:
        answer += 1
    print(answer)
else:
    print((n-1)//(k-1) + 1)
# ✌️✌️