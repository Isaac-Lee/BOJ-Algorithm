x11, y11, x12, y12 = map(int, input().split())
x21, y21, x22, y22 = map(int, input().split())
x = [x11, x12, x21, x22]
y = [y11, y12, y21, y22]
print(max((max(x)-min(x)), (max(y)-min(y)))**2)
