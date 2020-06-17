alpa = [0] * 26
for c in input():
    alpa[ord(c)-ord('a')] += 1
for n in alpa:
    print(n, end=" ")