MAX = 21252
p_mod = 23
e_mod = 28
i_mod = 33
min_p = 23*16
min_e = 28*14
min_i = 33*12

case = 1
while True:
    p,e,i,d = map(int, input().split())
    if [p,e,i,d] == [-1,-1,-1,-1]:
        break
    p = (p + (min_p-d)) % p_mod
    e = (e + (min_e-d)) % e_mod
    i = (i + (min_i-d)) % i_mod

    peak = [0] * (MAX+2)
    for pd in range(p, MAX+1, p_mod):
        peak[pd] += 1
    for ed in range(e, MAX+1, e_mod):
        peak[ed] += 1
    for id in range(i, MAX+1, i_mod):
        peak[id] += 1
    days = 1
    for i in range(1, MAX+1):
        if peak[i] == 3:
            days = i
            break
    print(f'Case {case}: the next triple peak occurs in {days} days.')
    case += 1
