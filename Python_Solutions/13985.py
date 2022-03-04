s = input()
a, b, c = map(int, (s[0], s[4], s[8]))
print('YES' if a+b == c else 'NO')