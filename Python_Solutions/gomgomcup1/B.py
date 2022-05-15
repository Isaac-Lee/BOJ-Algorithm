name = set()
count = 0
for _ in range(int(input())):
    id_name = input()
    if id_name == 'ENTER':
        name = set()
        continue
    if id_name in name:
        continue
    name.add(id_name)
    count += 1
print(count)
