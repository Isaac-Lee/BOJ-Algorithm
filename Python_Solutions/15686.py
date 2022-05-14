from itertools import combinations
import sys

def calc_dist(chicken, house):
    c_x, c_y = chicken
    h_x, h_y = house
    return abs(c_x-h_x)+abs(c_y-h_y)

N, M = map(int, input().split())
m = []
house = []
chicken = []
c_distance = {}
answer = sys.maxsize

for i in range(N):
    tmp = []
    for j, c in enumerate(map(int, input().split())):
        if c == 1:
            house.append((i, j))
        if c == 2:
            chicken.append((i, j))
        tmp.append(c)
    m.append(tmp)

for d in range(1, M+1):
    for comb in combinations(chicken, d):
        c_d = 0
        for h in house:
            c_d += min(map(lambda x: calc_dist(h, x), comb))
        answer = min(answer, c_d)
print(answer)