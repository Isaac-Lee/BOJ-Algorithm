t = input()
tl = t.split()
h=int(tl[0])
m=int(tl[1])
if (m-45) <0:
    m = 60+(m-45)
    if h !=0:
        h -= 1
    elif h ==0:
        h =23
else:
    m-=45
print(h,m)