from collections import deque
import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(g, r, c):
    result = 0
    s = deque()
    s.append([0, 0, g[0][0]])
    while s:
        x, y, visit_c = s.popleft()
        for i in range(4):
            next_x = x+dx[i]
            next_y = y+dy[i]
            if not (0<=next_x<r and 0<=next_y<c):
                continue
            if g[next_x][next_y] not in visit_c:
                s.append([next_x, next_y, visit_c+g[next_x][next_y]])
                result = max(result, len(visit_c)+1)
    return result


if __name__ == '__main__':
    r,c = map(int, input().split())
    g = [list(input().strip()) for _ in range(r)]
    print(bfs(g, r, c))