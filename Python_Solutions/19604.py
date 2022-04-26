bl_x = 100
bl_y = 100
tr_x = 0
tr_y = 0
for _ in range(int(input())):
    x,y = map(int, input().split(","))
    bl_x = min(bl_x, x)
    bl_y = min(bl_y, y)
    tr_x = max(tr_x, x)
    tr_y = max(tr_y, y)
print(f'{bl_x-1},{bl_y-1}')
print(f'{tr_x+1},{tr_y+1}')
