import math

n = int(input())

if n == 1:
    print('*')
else:
    for i in range(2 * n):
        if i % 2 == 1:
            print(' ' + '*' + ' *' * (math.floor(n / 2 - 1)))
        else:
            print('*' + ' *' * (math.ceil(n / 2 - 1)))