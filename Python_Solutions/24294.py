l = []
for _ in range(4):
    l.append(int(input()))
w1,h1,w2,h2 = l
print(w1+w2+h1*2+h2*2+4+(abs(w1-w2)))