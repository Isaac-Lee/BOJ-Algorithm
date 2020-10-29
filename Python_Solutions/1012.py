import sys
sys.setrecursionlimit(10**6)

def dfs(farm, m, n, x, y):
    farm[x][y] = 0
    desX = [1, -1, 0, 0]
    desY = [0, 0, 1, -1]
    for i in range(4):
        newX = x + desX[i]
        newY = y + desY[i]
        if 0 <= newX < m and 0 <= newY < n:
            if farm[newX][newY] == 1:
                dfs(farm, m, n, newX, newY)


def worms(m, n, k):
    farm = [[0 for _ in range(n)] for _ in range(m)]
    worm = 0
    for _ in range(k):
        x, y = map(int, input().split())
        farm[x][y] = 1
    for i in range(m):
        for j in range(n):
            if farm[i][j] == 1:
                worm += 1
                dfs(farm, m, n, i, j)
    return worm



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        print(worms(m, n, k))