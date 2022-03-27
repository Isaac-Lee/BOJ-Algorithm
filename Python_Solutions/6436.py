plopi = 1860000
file = 1
while True:
    s = int(input())
    if s == 0:
        break
    s = s/2
    s += s/2
    print(f'File #{file}')
    print(f'John needs {int(s//plopi+1)} floppies.\n')
    file += 1
