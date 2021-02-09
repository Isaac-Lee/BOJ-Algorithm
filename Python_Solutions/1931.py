import sys
N = int(input())

meeting = []
for _ in range(N):
    x = list(map(int, sys.stdin.readline().split()))
    meeting.append(x)

meeting.sort(key=lambda x: (x[1], x[0]))

answer = 0
t = 0
for i in range(N):
    m = meeting.pop(0)
    if m[0] >= t:
        t = m[1]
        answer += 1
    else:
        continue

print(answer)