n = int(input())
x, y = map(int, input().split())

for _ in range(1, n):
    cmd, val = input().split()
    if cmd == 'E':
        x += int(val)
    elif cmd == 'W':
        x -= int(val)
    elif cmd == 'N':
        y += int(val)
    elif cmd == 'S':
        y -= int(val)
    elif cmd == 'NE':
        val = (int(val)**2/2)**0.5
        x += val
        y += val
    elif cmd == 'NW':
        val = (int(val)**2/2)**0.5
        x -= val
        y += val
    elif cmd == 'SE':
        val = (int(val)**2/2)**0.5
        x += val
        y -= val
    elif cmd == 'SW':
        val = (int(val)**2/2)**0.5
        x -= val
        y -= val

print(f'{x:.8f}', f'{y:.8f}')