import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  score = []
  MAX_I = n
  answer = 0
  for _ in range(n):
    P, I = map(int, input().split())
    score.append((P, I))
  score.sort()
  for i in range(n):
    P, I = score[i]
    if I <= MAX_I:
      answer += 1
      MAX_I = I
  print(answer)