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
    visited = set()
    days = 0

    for start in starts:
        queue.append(start)

    while queue:
        next = len(queue)
        for _ in range(next):
            now = queue.popleft()
            x, y = now
            tomato[x][y] = 1
            for direction in directions:
                dx, dy = direction
                new_x, new_y = x+dx, y+dy
                if is_inside(M, N, new_x, new_y):
                    if tomato[new_x][new_y] != 0:
                        continue
                    if (new_x, new_y) in visited:
                        continue
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
        days += 1
    return days-1


def is_all_ripe(tomato):
    for tomatoes in tomato:
        if 0 in tomatoes:
            return False
    return True


if __name__ == '__main__':
    M, N = [int(x) for x in input().split()]
    tomato = []
    starts = []
    for x in range(N):
        tomatoes = []
        for y, t in enumerate(input().split()):
            tomatoes.append(int(t))
            if t == '1':
                starts.append((x, y))
        tomato.append(tomatoes)
    answer = bfs(starts, tomato, M, N)
    if is_all_ripe(tomato):
        print(answer)
    else:
        print(-1)
