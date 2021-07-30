from collections import deque
import sys

d = deque()

for _ in range(int(sys.stdin.readline())):
  d.append(int(sys.stdin.readline()))

count = 0
m = 0
while d:
  i = d.pop()
  if i <= m:
    continue
  else:
    m = i
    count += 1

print(count)