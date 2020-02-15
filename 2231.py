n = int(input())

answer = 0
for i in range(0,n+1):
    nl = list(map(int, str(i)))
    sum_n = i + sum(nl)
    if sum_n == n:
        answer = i
        break
print(answer)

'''
N = int(input())
print_num = 0
for i in range(1, N+1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num)
    if(sum_num == N):
        print_num = i
        break
print(print_num)
'''