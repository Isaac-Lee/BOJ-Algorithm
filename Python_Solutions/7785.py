n = int(input())
employ = set()

for _ in range(n):
    name, cmd = input().split()
    if cmd == 'enter':
        employ.add(name)
    else:
        employ.remove(name)
for name in sorted(employ, reverse=True):
    print(name)
    