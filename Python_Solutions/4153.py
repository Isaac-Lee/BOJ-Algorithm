def isRightTriangle(num):
    z = num.pop(num.index(max(num)))
    x, y = num
    if x**2 + y **2 == z**2:
        print("right")
    else:
        print("wrong")

while True:
    nlist = list(map(int, input().split()))
    if nlist[0] == 0 and nlist[1] == 0 and nlist[2] == 0:
        break
    else:
        isRightTriangle(nlist)