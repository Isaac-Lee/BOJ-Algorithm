import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    num = []
    for _ in range(N):
        num.append(input()[:-1])
    num.sort()
    prev = num[0]
    isOk = True
    for i in range(1, N):
        isSame = True
        for j in range(min(len(prev), len(num[i]))):
            if prev[j] != num[i][j]:
                isSame = False
        if isSame:
            isOk = False
            break
        prev = num[i]
    if isOk:
        print("YES")
    else:
        print("NO")
