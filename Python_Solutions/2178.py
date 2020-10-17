def bfs(maze, n, m):
    visit = set()
    answer = []
    for _ in range(n):
        answer.append([0 for _ in range(m)])
    queue = [(0, 0)]
    answer[0][0] = 1
    destination = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    while queue:
        node = queue.pop(0)
        if node not in visit:
            x = node[0]
            y = node[1]
            visit.add(node)
            if x == n-1 and y == m-1:
                break
            for i in range(4):
                addX = destination[i][0]
                addY = destination[i][1]
                newX = x+addX
                newY = y+addY
                value = 0
                if 0 <= newX <= n-1 and 0 <= newY <= m-1:
                    value = maze[newX][newY]
                if value:
                    answer[newX][newY] = answer[x][y]+1
                    queue.append((x+addX, y+addY))
    return answer[n-1][m-1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input())))
    print(bfs(maze, n, m))