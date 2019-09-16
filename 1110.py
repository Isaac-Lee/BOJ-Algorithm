n = input()
c = 0
def count(re):
    global c, n
    if len(re) == 1:
        re = '0' + re
    if len(str(int(re[0]) + int(re[1])))==2:
        re = re[1] + str(int(re[0]) + int(re[1]))[1]
    elif len(str(int(re[0]) + int(re[1])))==1:
        re = re[1] + str(int(re[0]) + int(re[1]))[0]
    c+=1
    if int(re) == int(n):
        return
    count(re)

count(n)

print(c)
