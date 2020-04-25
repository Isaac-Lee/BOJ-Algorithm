from functools import reduce
n = reduce(lambda x, y: x*y, map(int, input().split()))
numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    print(numbers[i]-n, end=' ')

# r=lambda:map(int,input().split());A,B=r()
# for x in r():print(x-A*B)