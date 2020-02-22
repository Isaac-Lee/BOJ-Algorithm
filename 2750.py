answer=[]
for _ in range(int(input())):
    answer.append(int(input()))

# 정렬하는 부분
for i in range(len(answer)):
    for j in range(len(answer)-i-1):
        if answer[j] > answer[j+1]:
            temp = answer[j]
            answer[j] = answer[j+1]
            answer[j+1] = temp
for n in answer:
    print(n)