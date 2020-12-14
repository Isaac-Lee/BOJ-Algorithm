t = int(input())
for _ in range(t):
    n = int(input())
    p = input().split()
    malePref = {}
    femalePref = {}
    malePartner = {}
    femalePartner = {}
    for i in range(n):
        malePref[p[i]] = list(map(lambda x: x, input()[2:]))
    for i in range(n, n+n):
        femalePref[p[i]] = list(map(lambda x: x, input()[2:]))

    isReject = True
    while isReject:
        isReject = False
        for male in malePref:
            if male in malePartner:
                continue
            female = malePref[male].pop(0)
            if female not in femalePartner:
                femalePartner[female] = male
                malePartner[male] = female
            else:
                prevMale = femalePartner[female]
                if femalePref[female].index(prevMale) > femalePref[female].index(male):
                    malePartner.pop(prevMale)
                    malePartner[male] = female
                    femalePartner[female] = male
                isReject = True
    for male in sorted(malePartner):
        print(male, malePartner[male])
    print()