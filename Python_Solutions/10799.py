s = input()
b = 0
prev = ''
total = 0

for c in s:
    if c == '(':
        b += 1
    elif c == ')':
        if prev == '(':
            b -= 1
            total += b
        elif prev == ')':
            b -= 1
            total += 1
    prev = c

print(total)