nm = [int(k) for k in input().split()]
nList = [[] for i in range(nm[0])]
re=[]
mNum ={}
for i in range(nm[1]):
    m = [int(m) for m in input().split()]
    nList[m[0]-1].append(m[1]-1)
    nList[m[1]-1].append(m[0]-1)
print(nList)
for j in range(nm[0]):
    mNum[j] = len(nList[j])
print(mNum)
for k in range(nm[1]):
    mini = list(mNum.values()).index(min(mNum.values()))
    re.append(mini)
    print(mini)
    for index in range(nm[0]):
        print(index)
        if index != mini:
            print(nList[index])
            nList[index].remove(mini)
            mNum[index] -= 1
# print(nList)
# print(mNum)
# print(re)

## 미해결