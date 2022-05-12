from collections import deque

def BFS(start, target):
    count = 0
    if start > target:
        return -1
    queue = deque()
    queue.append((start, 1))
    while queue:
        n, count = queue.popleft()
        mul2 = n*2
        add1 = int(f'{n}1')
        if mul2 == target or add1 == target:
            return count + 1
        else:
            if mul2 <= target:
                queue.append((mul2, count+1))
            if add1 <= target:
                queue.append((add1, count+1))
    return -1

if __name__ == '__main__':
    a,b = map(int, input().split())
    print(BFS(a, b))
