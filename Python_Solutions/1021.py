def move(p, num):
    right = 0
    left = 0
    while True:
        if Deque[p] == num:
            left = len(Deque) - right
            break
        else:
            right += 1
            p += 1
    if right < left:
        if len(Deque) == 0:
            return 0, right
        return p, right
    else:
        if len(Deque) == 0:
            return 0, left
        return p, left


N, M = list(map(int, input().split(' ')))
Deque = [i for i in range(1, N + 1)]
pick_num = list(map(int, input().split(' ')))
count = 0
for j in pick_num:
    Aft_Pointer, Aft_Count = move(0, j)
    temp = Deque[:Aft_Pointer]
    Deque = Deque[Aft_Pointer + 1:] + temp
    count = count + Aft_Count
print(count)