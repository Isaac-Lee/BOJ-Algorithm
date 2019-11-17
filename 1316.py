n = int(input())
l = []
c = 0
for i in range(n):
    w = input()
    if len(w) !=1:
        for j in range(1, len(w)):
            if w[j] == w[j - 1]:
                pass
            elif w[j] in l:
                c -= 1
                break
            else:
                l.append(w[j-1])
    c += 1
    l=[]
print(c)