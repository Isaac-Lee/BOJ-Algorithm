n = int(input())
sec = []
for i in range(n):
    sec.append(input())

score = []
for n in sec:
    cur = ' '
    sco = 0
    resco = 0
    for i in range(len(n)):
        cur = n[i]
        if cur == 'O':
            sco +=1
            resco += sco
        elif cur == 'X':
            sco = 0
    score.append(resco)

for sco in score:
    print(sco)