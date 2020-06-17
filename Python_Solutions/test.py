a=input('입력하세요\n')
while True:
        new = a.replace('~',' ').replace('!',' ').replace('@',' ').replace('#',' ').replace('$',' ').replace('%',' ').replace('^',' ').replace('&',' ').replace('*',' ').replace('-',' ').replace('_',' ').replace('+',' ').replace('=',' ').replace('(',' ').replace(')',' ').replace('{',' ').replace('}',' ').replace('[',' ').replace(']',' ').replace(';',' ').replace(':',' ').replace('?',' ').replace('.',' ').replace(',',' ').replace('<',' ').replace('>',' ')
        break
print('**특수문자를 공백으로 바꾼 새 문자열')
print(new)      
newList = new.split()
newDict = {}
for x in newList:
    if x in newDict.keys():
        newDict[x] += 1
    else:
        newDict[x] = 1
print('** 단어별 빈도수')
for word, times in newDict.items():
    print(len(word))
    print(word, " "*(12 - len(word)), times)