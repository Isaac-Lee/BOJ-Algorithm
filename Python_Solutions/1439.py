s = input()
prev = int(s[0])
answer = [0, 0]
answer[prev] += 1
for i in range(1, len(s)):
    c = int(s[i])
    if c != prev:
        prev = c
        answer[c] += 1

print(min(answer))