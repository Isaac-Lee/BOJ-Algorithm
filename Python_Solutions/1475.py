import math

room_num = list(map(int, str(input())))
set_num = [0] * 9

for i in room_num:
    if i == 6 or i == 9:
        set_num[5] += 0.5
    else:
        set_num[i] += 1

print(math.ceil(max(set_num)))