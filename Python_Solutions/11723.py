import sys

M = int(input())
my_set = set()
for _ in range(M):
  temp = sys.stdin.readline().strip().split()
  if len(temp) == 1:
    cmd = temp[0]
    if cmd == "all":
      my_set = set([i for i in range(1, 21)])
    else:
      my_set = set()
  else:
    cmd, target = temp
    target = int(target)
    if cmd == "add":
      my_set.add(target)
    elif cmd == "check":
      print(1 if target in my_set else 0)
    elif cmd == "remove":
      my_set.discard(target)
    elif cmd == "toggle":
      if target not in my_set:
        my_set.add(target)
      else:
        my_set.discard(target)