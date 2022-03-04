apb, amb = map(int, input().split())
a = (apb+amb)/2
b = apb - a
if a<0 or b<0:
    print(-1)
elif a != int(a) or b != int(b):
    print(-1)
else:
    print(int(a), int(b))