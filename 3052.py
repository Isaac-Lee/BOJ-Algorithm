nlist = []
last =[]
for i in range(0,10):
    nlist.append(int(input()))
for n in nlist:
    last.append(n % 42)
last = set(last)
print(len(last))