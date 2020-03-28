import collections

n = int(input())
queue = collections.deque([])

for i in range(n):
    case = input().split()
    order = case[0]

    if order == 'push':
        queue.append(case[1])
    elif order == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        print(queue[0])
    elif order == 'back':
        print(queue[-1])
    else:
        print('xx')
