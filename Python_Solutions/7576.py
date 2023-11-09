from collections import deque

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_inside(M, N, x, y):
    if x < 0 or x > N-1:
        return False
    if y < 0 or y > M-1:
        return False
    return True


def bfs(starts, tomato, M, N):
    queue = deque()

    for start in starts:
        queue.append(start)

    while queue:
        x, y = queue.popleft()
        for direction in directions:
            dx, dy = direction
            new_x, new_y = x + dx, y + dy
            # 그래프 밖 좌표는 제외한다.
            if is_inside(M, N, new_x, new_y):
                # 이미 익힌 토마토와 토마토가 없는 칸은 건너뛴다.
                if tomato[new_x][new_y] == 0:
                    tomato[new_x][new_y] = tomato[x][y] + 1
                    queue.append((new_x, new_y))


def is_all_ripe(tomato):
    max_days = 0
    for tomatoes in tomato:
        for t in tomatoes:
            if t == 0:
                return 0
            max_days = max(t, max_days)
    return max_days


if __name__ == '__main__':
    M, N = map(int, input().split())
    tomato = [list(map(int, input().split())) for _ in range(N)]
    starts = []
    for x in range(N):
        for y in range(M):
            if tomato[x][y] == 1:
                starts.append((x, y))
    bfs(starts, tomato, M, N)
    answer = is_all_ripe(tomato)
    if answer > 0:
        print(answer-1)
    else:
        print(-1)
