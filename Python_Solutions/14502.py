from itertools import combinations
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(N, M, wall, virus, count):
    visit = set(virus)
    total = count
    queue = deque()
    queue.extend(virus)
    while queue:
        x, y = queue.popleft()
        total -= 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (nx, ny) in wall:
                continue
            if (nx, ny) in visit:
                continue
            if 0 <= nx < N and 0 <= ny < M:
                visit.add((nx, ny))
                queue.append((nx, ny))
    return total

if __name__ == '__main__':
    N, M = map(int, input().split())
    m = []
    safe = []
    safe_count = N*M
    wall = set()
    virus = []

    for i in range(N):
        tmp = input().split()
        for j in range(M):
            c = int(tmp[j])
            if c == 0:
                safe.append((i, j))
            elif c == 1:
                safe_count -= 1
                wall.add((i, j))
            elif c == 2:
                virus.append((i, j))
            tmp.append(c)

    MAX_AREA = 0
    for comb in combinations(safe, 3):
        new_wall = wall.copy()
        for s in comb:
            new_wall.add(s)
        MAX_AREA = max(MAX_AREA, bfs(N, M, new_wall, virus, safe_count-3))
    print(MAX_AREA)

