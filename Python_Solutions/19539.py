n = int(input())
h_list = list(map(int, read().split()))
h_sum = sum(h_list)
t = h_sum//3

if h_sum % 3 != 0:
    print('NO')
else:
    for h in h_list:
        t -= (h//2)
    if t > 0:
        print('NO')
    else:
        print('YES')