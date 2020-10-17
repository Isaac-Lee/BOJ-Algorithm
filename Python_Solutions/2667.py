def dfs(house, x, y, n, count):
    house[x][y] = 0
    destination = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for i in range(4):
        addX = destination[i][0]
        addY = destination[i][1]
        newX = x + addX
        newY = y + addY
        if 0 <= newX <= n - 1 and 0 <= newY <= n - 1:
            if house[newX][newY] == 1:
                count = dfs(house, newX, newY, n, count+1)
    return count


def Numbering(house, n):
    households = []
    for i in range(n):
        for j in range(n):
            if house[i][j] == 1:
                households.append(dfs(house, i, j, n, 1))
    return households, len(households)


if __name__ == '__main__':
    n = int(input())
    house = []
    for _ in range(n):
        house.append(list(map(int, input())))
    answer = Numbering(house, n)
    print(answer[1])
    for i in sorted(answer[0]):
        print(i)