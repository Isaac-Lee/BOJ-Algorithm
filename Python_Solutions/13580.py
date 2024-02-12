c = sorted(list(map(int, input().split())))
if c[0]==c[1] or c[1]==c[2] or c[0]+c[1]==c[2]:
    print('S')
else:
    print('N')