string = input().upper()
stringSet = set()
stringDic = {}
stringList = []
for n in string:
    stringSet.add(n)
for v in stringSet:
    stringDic[v] = 0
for s in string:
    for k in stringSet:
        if s == k:
            stringDic[k] += 1
for k in stringDic:
    stringList.append(stringDic[k])
c=0
re = True
if stringList.count(max(stringList)) >1:
    re = False

if re:
    print(list(stringDic.keys())[stringList.index(max(stringList))])
else:
    print("?")