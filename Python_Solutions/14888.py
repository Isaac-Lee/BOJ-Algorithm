c = int(input())
num_list = list(map(int, input().split()))
calc_list = list(map(int, input().split()))


def make_calc_dict(calc_list):
    calc_dict = dict()
    for i, c in enumerate(calc_list):
        calc_dict[i] = c

    return calc_dict


def calc(init_num, num, calc_num):
    if calc_num == 0:
        return init_num + num
    elif calc_num == 1:
        return init_num - num
    elif calc_num == 2:
        return init_num * num
    elif calc_num == 3:
        if init_num < 0:
            return -(-init_num // num)
        else:
            return init_num // num


calc_dict = make_calc_dict(calc_list)

result_list = []


def solve(num_list, calc_dict):
    if len(num_list) == 1:
        result_list.append(num_list[0])
        return 0
    else:
        # 계산에 사용 될 수
        init_num = num_list.pop(0)
        temp_num = num_list[0]

        # 백트래킹
        for key, value in calc_dict.items():
            # 0이면 다음 경우로
            if value == 0:
                continue
            else:
                # 해당 계산을 수행
                num = calc(init_num, temp_num, key)
                calc_dict[key] = calc_dict[key] - 1

                if len(num_list) == 0:
                    deliver_list = [num]
                else:
                    deliver_list = [num] + num_list[1:]
                solve(deliver_list, calc_dict)
                calc_dict[key] = calc_dict[key] + 1


solve(num_list, calc_dict)
print(max(result_list))
print(min(result_list))