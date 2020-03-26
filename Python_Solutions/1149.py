import sys


def minCost(n):
    cost[0] = list(map(int, sys.stdin.readline().split()))
    for i in range(1, n):
        case = list(map(int, sys.stdin.readline().split()))
        cost[1] = case
        cost[2][0] = cost[1][0] + min(cost[0][1], cost[0][2])
        cost[2][1] = cost[1][1] + min(cost[0][0], cost[0][2])
        cost[2][2] = cost[1][2] + min(cost[0][0], cost[0][1])
        cost[0] = cost[2]
        cost[2] = [0, 0, 0]
    return min(cost[0])


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    cost = [[0, 0, 0]]*3
    print(minCost(n))