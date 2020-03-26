Case = int(input())
for _ in range(Case):
    x_1, y_1, r_1, x_2, y_2, r_2 = list(map(int, input().split()))
    d = ((x_1 - x_2) ** 2) + ((y_1 - y_2) ** 2)
    r_sum = (r_1 + r_2) ** 2
    r_diff = (r_1 - r_2) ** 2

    if (d == 0):

        if (r_1 == r_2):
            print(-1)
        else:
            print(0)
    else:
        if ((d == r_sum) or (d == r_diff)):
            print(1)
        elif ((d < r_sum) and (d > r_diff)):
            print(2)
        else:
            print(0)