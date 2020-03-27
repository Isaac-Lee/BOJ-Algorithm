a, b = list(map(int, input().split()))
if a < b:
    a, b = b, a

while 1:
    qou = a//b
    rem = a-qou*b
    if rem == 0:
        gcm = rem
        lcm = a*b / gcm
        print(gcm)
        print(lcm)
        break