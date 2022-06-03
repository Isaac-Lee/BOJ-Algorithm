Tetromino = {
    0: {
        "dx": [0, 0, 0, 0],
        "dy": [0, 1, 2, 3],
        "mx": 0,
        "my": 3,
    },
    1: {
        "dx": [0, 1, 2, 3],
        "dy": [0, 0, 0, 0],
        "mx": 3,
        "my": 0,
    },
    2: {
        "dx": [0, 1, 0, 1],
        "dy": [0, 0, 1, 1],
        "mx": 1,
        "my": 1,
    },
    3: {
        "dx": [0, 0, 1, 0],
        "dy": [0, 1, 1, 2],
        "mx": 1,
        "my": 2,
    },
    4: {
        "dx": [0, 1, 2, 1],
        "dy": [0, 0, 0, 1],
        "mx": 2,
        "my": 1,
    },
    5: {
        "dx": [0, 1, 1, 2],
        "dy": [1, 0, 1, 1],
        "mx": 2,
        "my": 1,
    },
    6: {
        "dx": [0, 1, 1, 1],
        "dy": [1, 0, 1, 2],
        "mx": 1,
        "my": 2,
    },
    7: {
        "dx": [0, 1, 1, 2],
        "dy": [0, 0, 1, 1],
        "mx": 2,
        "my": 1,
    },
    8: {
        "dx": [0, 1, 1, 0],
        "dy": [1, 0, 1, 2],
        "mx": 1,
        "my": 2,
    },
    9: {
        "dx": [0, 0, 1, 1],
        "dy": [0, 1, 1, 2],
        "mx": 1,
        "my": 2,
    },
    10: {
        "dx": [0, 1, 1, 2],
        "dy": [1, 0, 1, 0],
        "mx": 2,
        "my": 1,
    },
    11: {
        "dx": [0, 1, 2, 2],
        "dy": [0, 0, 0, 1],
        "mx": 2,
        "my": 1,
    },
    12: {
        "dx": [0, 0, 1, 0],
        "dy": [0, 1, 0, 2],
        "mx": 1,
        "my": 2,
    },
    13: {
        "dx": [0, 0, 1, 2],
        "dy": [0, 1, 1, 1],
        "mx": 2,
        "my": 1,
    },
    14: {
        "dx": [1, 1, 1, 0],
        "dy": [0, 1, 2, 2],
        "mx": 1,
        "my": 2,
    },
    15: {
        "dx": [0, 1, 2, 2],
        "dy": [1, 1, 1, 0],
        "mx": 2,
        "my": 1,
    },
    16: {
        "dx": [0, 1, 1, 1],
        "dy": [0, 0, 1, 2],
        "mx": 1,
        "my": 2,
    },
    17: {
        "dx": [0, 0, 1, 2],
        "dy": [0, 1, 0, 0],
        "mx": 2,
        "my": 1,
    },
    18: {
        "dx": [0, 0, 0, 1],
        "dy": [0, 1, 2, 2],
        "mx": 1,
        "my": 2,
    },
}

def calcSum(C, T, x, y):
    dx = Tetromino[T]["dx"]
    dy = Tetromino[T]["dy"]
    target = []
    for d in range(4):

        # try:
        #     target.append(C[x + dx[d]][y + dy[d]])
        # except:
        #     print(x, y, T)
        #     print(x + dx[d], y + dy[d])
        #     mx = Tetromino[T]["mx"]
        #     my = Tetromino[T]["my"]
        #     print(x+mx, y+my)
        #     exit()

        target.append(C[x+dx[d]][y+dy[d]])
    return sum(target)

def isInBound(n, m, T, x, y):
    mx = Tetromino[T]["mx"]
    my = Tetromino[T]["my"]
    return ((x + mx) < n) and ((y + my) < m)

N, M = map(int, input().split())
cell = []
answer = 0

for _ in range(N):
    cell.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        for k in range(19):
            if isInBound(N, M, k, i, j):
                answer = max(answer, calcSum(cell, k, i, j))

print(answer)
