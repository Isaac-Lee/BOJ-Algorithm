n = int(input())

for i in range(n):
    if i%2 == 1:
        print(' '+'*'+' *'*(n-1))
    else:
        print('*'+' *'*(n-1))