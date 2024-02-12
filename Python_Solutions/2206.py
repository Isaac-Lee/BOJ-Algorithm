from collections import deque

n,m = map(int, input().split())
road = []
visited = [[[0 for j in range(m)] for i in range(n)] for k in range(2)]
x_move = [1, -1, 0, 0]
y_move = [0, 0, 1, -1]


def BFS(n, m, road):
    visited[0][0][0] = 1
    queue = deque([(0, 0, 0)])

    while queue:
        c = queue.popleft()
        w = c[0]
        x = c[1]
        y = c[2]
        if x == n - 1 and y == m - 1:
            return visited[w][x][y]

        for i in range(4):
            nw = w
            nx = x + x_move[i]
            ny = y + y_move[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nw][nx][ny]:
                continue
            if road[nx][ny] == 0:
                visited[nw][nx][ny] = visited[w][x][y] + 1
                queue.append([nw, nx, ny])
            if road[nx][ny] == 1 and nw == 0:
                visited[1][nx][ny] = visited[w][x][y] + 1
                queue.append([1, nx, ny])

    return -1

if __name__ == '__main__':
    for _ in range(n):
        road.append(list(map(int, input())))
    print(BFS(n, m, road))
