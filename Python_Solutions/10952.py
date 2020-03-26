while(True):
    nlist = [int(k) for k in input().split()]
    if nlist[0] ==0 and nlist[1] == 0:
        break
    else:
        print(nlist[0] + nlist[1])