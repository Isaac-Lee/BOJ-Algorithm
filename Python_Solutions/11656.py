word = input()
s = []
for i in range(len(word)):
    s.append(word[i:])
s.sort()
for a in s:
    print(a)