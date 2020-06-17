n, m = map(int, input().split())
map = []
for i in range(n):
    map.append([])
    nums = input().split()
    for j in range(m):
        if j == 0:
            map[i].append(int(nums[0]))
        else:
            map[i].append(int(nums[j]) + map[i][j-1])

k = int(input())
for _ in range(k):
    i, j, x, y = input().split()
    i = int(i)-1
    j = int(j)-1
    x = int(x)-1
    y = int(y)-1
    answer = 0
    for k in range(i, x+1):
        if j == 0:
            answer += map[k][y]
        else:
            answer += map[k][y] - map[k][j-1]
    print(answer)