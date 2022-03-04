SKH = list(map(int,input().split()))
skh = ["Soongsil", "Korea", "Hanyang"]

if sum(SKH) < 100:
    print(skh[SKH.index(min(SKH))])
else:
    print("OK")