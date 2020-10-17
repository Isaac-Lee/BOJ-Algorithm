from collections import deque

p, m = map(int, input().split())
players = []
for i in range(p):
    a = input().split()
    players.append([int(a[0]), a[1]])

players.sort(key=lambda x: x[0])

players = deque(players)

rooms = []
while len(players) > 0:
    count = 0
    room = []
    while count < m:
        if len(players) <= 0:
            break
        if count >= p:
            break
        player = players.popleft()
        count += 1
        if player[0] > room[0][0]+10:
            players.append()
            continue
        elif player[0] < room[0][0]-10:
            continue
        else:
            room.append(players.popleft())
    room.sort(key=lambda x: x[1])
    rooms.append(room)

for room in rooms:
    print("Started!")
    for player in room:
        print(player[0], player[1])