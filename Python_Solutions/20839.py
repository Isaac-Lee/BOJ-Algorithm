x,y,z = map(int,input().split())
x_,y_,z_ = map(int,input().split())
if x_>=x and y_>=y and z_>=z:
    print('A')
elif x_>=x/2 and y_>=y and z_>=z:
    print('B')
elif y_>=y and z_>=z:
    print('C')
elif y_>=y/2 and z_>=z/2:
    print('D')
else:
    print('E')
