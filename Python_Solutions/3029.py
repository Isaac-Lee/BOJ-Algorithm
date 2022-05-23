a = list(map(int, input().split(":")))
b = list(map(int, input().split(":")))
a = a[0]*3600 + a[1]*60 + a[2]
b = b[0]*3600 + b[1]*60 + b[2]

if b < a:
    b += 24*3600

answer = b-a
if answer == 0:
    answer += 24*3600
hour = answer//3600
answer %= 3600
mint = answer//60
answer %= 60
sec = answer
print(f'{hour:02}:{mint:02}:{sec:02}')
