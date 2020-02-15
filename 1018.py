N, M = map(int, input().split())
map_list = [list(input()) for _ in range(N)]

min_num = None

for i in range(N - 7):
    for j in range(M - 7):
        num1, num2 = 0, 0
        # W
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if ((k + l - i - j) % 2 == 0):
                    if (map_list[k][l] == 'B'):
                        num1 += 1
                else:
                    if (map_list[k][l] == 'W'):
                        num1 += 1

        # B
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if ((k + l - i - j) % 2 == 0):
                    if (map_list[k][l] == 'W'):
                        num2 += 1
                else:
                    if (map_list[k][l] == 'B'):
                        num2 += 1

        change_box = num1 if num1 < num2 else num2
        if (min_num is None):
            min_num = change_box
        else:
            min_num = change_box if min_num > change_box else min_num

print(min_num)