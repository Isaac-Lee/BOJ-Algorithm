n, r, c = map(int, input().split())
answer = 0

while n > 0:
    n -= 1
    t = 2**n
    if r < t and c < t:
        continue
    elif r < t <= c:
        answer += t*t
        c -= t
    elif c < t <= r:
        answer += t*t*2
        r -= t
    else:
        answer += t*t*3
        r -= t
        c -= t

print(answer)