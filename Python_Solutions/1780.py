import sys


def cut(x, y, n):
    global blue, white, red
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                p_n = n // 3
                cut(x, y, p_n)
                cut(x, y + p_n, p_n)
                cut(x + p_n, y, p_n)
                cut(x + p_n, y + p_n, p_n)
                cut(x, y + p_n*2, p_n)
                cut(x + p_n*2, y, p_n)
                cut(x + p_n, y + p_n * 2, p_n)
                cut(x + p_n * 2, y + p_n, p_n)
                cut(x + p_n*2, y + p_n*2, p_n)
                return

    if check == -1:
        white += 1
        return
    elif check == 0:
        blue += 1
        return
    else:
        red += 1
        return


n = int(sys.stdin.readline())
paper = []

white = 0
blue = 0
red = 0

for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))


cut(0, 0, n)
print(white)
print(blue)
print(red)