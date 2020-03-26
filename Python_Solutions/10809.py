aList = []
for i in range(26):
    aList.append(-1)

S = input()

for c in S:
    if aList[ord(c)-97] == -1:
        aList[ord(c)-97] = S.index(c)
    else:
        pass
string = ""
for s in aList:
    if aList.index(s) == 0:
        string += str(s)
    else:
        string += " "+str(s)
print(string)