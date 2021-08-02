for i in range(int(input())):
    s = list(input())
    answer = 0
    for j in s:
        if j == '(':
            answer += 1
        elif j == ')':
            answer -= 1
        if answer < 0:
            print('NO')
            break
    if answer > 0:
        print('NO')
    elif answer == 0:
        print('YES')

