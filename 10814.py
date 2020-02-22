l = []
for _ in range(int(input())):
    nl = list(input().split())
    nl[0] = int(nl[0])
    l.append(nl)
l.sort(key= lambda x: x[0])
for p in l:
    print(p[0], p[1])