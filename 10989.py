import sys

# 인덱싱을 이용한 풀
answer=[0]*10001
for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline()
    answer[int(a)] += 1

for i in range(len(answer)):
    if answer[i] != 0:
        for k in range(answer[i]):
            print(i)