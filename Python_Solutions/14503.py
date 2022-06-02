import copy
import time
import os
def printCell(cell, r, c, d):
    rob = ["▲", "▶", "▼", "◀"]
    p_c = copy.deepcopy(cell)
    p_c[r][c] = rob[d]
    for row in p_c:
        print(*row)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
d_r = [-1, 0, 1, 0]
d_c = [0, 1, 0, -1]

cell = []
for i in range(N):
    cell.append(list(map(int, input().split())))

clean = 0
l_count = 0
while True:

    # 1. 현재 위치를 청소한다.
    if cell[r][c] == 0:
        clean += 1
        cell[r][c] = 2

    # 2.b. 2a번 단계가 연속으로 네 번 실행되었을 경우,
    if l_count == 4:
        back = (d + 2) % 4
        b_r, b_c = r + d_r[back], c + d_c[back]
        if cell[b_r][b_c] == 1:
            # 바로 뒤쪽이 벽이라면 작동을 멈춘다.
            break
        else:
            # 그렇지 않다면 한 칸 후진한다.
            r, c = b_r, b_c
            l_count = 0
    else:
        left = (d+3)%4
        l_r, l_c = r+d_r[left], c+d_c[left]
        # 2.a. 현재 위치의 바로 왼쪽에 아직 청소하지 않은 빈 공간이 존재한다면,
        if cell[l_r][l_c] == 0:
            # 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다.
            r, c = l_r, l_c
            l_count = 0
        else:
            # 그렇지 않을 경우, 왼쪽 방향으로 회전한다.
            l_count += 1
        d = left

print(clean)
