import sys


def cut(x, y, n):
    global blue, white
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                cut(x, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                return

    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return


n = int(sys.stdin.readline())
paper = []

white = 0
blue = 0

for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))


cut(0, 0, n)
print(white)
print(blue)