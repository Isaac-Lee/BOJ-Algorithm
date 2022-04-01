from itertools import combinations
l, c = map(int, input().split())
c = sorted(input().split())
c = list(combinations(c, l))
for word in c:
    flag = False
    for i in ['a', 'e', 'i', 'o', 'u']:
        if i in word:
            lword = list(word)
            for j in ['a', 'e', 'i', 'o', 'u']:
                if j in lword:
                    lword.remove(j)
            if len(lword) >= 2:
                flag = True
                break
    if flag:
        for i in range(l):
            print(word[i], end="")
        print()