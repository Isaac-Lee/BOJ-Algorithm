answer = []
for i in range(int(input())):
    case = int(input())
    if case == 0:
        answer.pop()
    else:
        answer.append(case)
print(sum(answer))