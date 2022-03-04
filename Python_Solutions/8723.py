l = sorted(list(map(int, input().split())))
if l.count(l[0]) == 3:
    print(2)
elif l.pop()**2 == (l.pop()**2 + l.pop()**2):
    print(1)
else:
    print(0)