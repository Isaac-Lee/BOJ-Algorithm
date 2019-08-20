num = int(input())
for i in range(0,num):
    print(' '*(num-1-i)+'*'*(i+1))
for i in range(1,num):
    print(' '*(i)+'*'*(num-i))