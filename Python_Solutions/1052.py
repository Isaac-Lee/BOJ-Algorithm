bottle, k = map(int, input().split())

answer = 0
while True:
    count = 0
    now_bottle = bottle

    while now_bottle > 0:
        if now_bottle % 2 != 0:
            count += 1
        now_bottle = now_bottle // 2
    if count <= k:
        break
    bottle += 1
    answer += 1

print(answer)