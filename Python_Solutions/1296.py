y = input()
names = [input() for _ in range(int(input()))]
names.sort()

y_love = [y.count('L'),
          y.count('O'),
          y.count('V'),
          y.count('E')]
names_loves = []
for name in names:
  names_loves.append([name.count('L'),
                     name.count('O'),
                     name.count('V'),
                     name.count('E')])
names_scores = []
for names_love in names_loves:
  L = y_love[0] + names_love[0]
  O = y_love[1] + names_love[1]
  V = y_love[2] + names_love[2]
  E = y_love[3] + names_love[3]
  names_scores.append(((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100)
print(names[names_scores.index(max(names_scores))])
  