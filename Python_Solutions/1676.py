n = int(input())

if n == 0:
  print(0)
else:
  count_0 = 0
  for i in range(2, n+1):
    if i%5 == 0: count_0 += 1
    if i%25 == 0: count_0 += 1
    if i%125 == 0: count_0 += 1
  print(count_0)