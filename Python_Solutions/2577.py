nlist = []
count = [0,0,0,0,0,0,0,0,0,0]
for i in range(0,3):
    nlist.append(int(input()))

nlist = str(nlist[0]*nlist[1]*nlist[2])

for n in nlist:
    if int(n) == 0:
        count[0]+=1
    elif int(n) == 1:
        count[1]+=1
    elif int(n) == 2:
        count[2] += 1
    elif int(n) == 3:
        count[3] += 1
    elif int(n) == 4:
        count[4] += 1
    elif int(n) == 5:
        count[5] += 1
    elif int(n) == 6:
        count[6] += 1
    elif int(n) == 7:
        count[7] += 1
    elif int(n) == 8:
        count[8] += 1
    elif int(n) == 9:
        count[9] += 1
    else:
        pass
for c in count:
    print(c)