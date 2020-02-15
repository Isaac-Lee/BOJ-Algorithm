M = int(input().split()[1])
nList = [int(i) for i in input().split()]
nList.sort()

answer = 0
for j in nList:
    for k in nList:
        for l in nList:
            if nList.index(j) != nList.index(k) and nList.index(k) != nList.index(l) and nList.index(j) != nList.index(l):
                if j + k + l <= M:
                    if answer <= j + k + l:
                        answer = j + k + l
print(answer)