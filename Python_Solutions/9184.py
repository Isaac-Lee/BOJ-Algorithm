import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

score = [[[0 for _ in range(21)] \
          for _ in range(21)] \
         for _ in range(21)]

for i in range(2):
    for j in range(2):
        for k in range(2):
            score[i][j][k] = 1
score[1][1][1] = 2


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if score[a][b][c] > 0:
        return score[a][b][c]
    if a < b < c:
        score[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        score[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return score[a][b][c]


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    result = w(a, b, c)
    print("w(%d, %d, %d) = %d" % (a, b, c, result))

