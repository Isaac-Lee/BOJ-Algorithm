answer = 0
prev = ""
s = input()
for c in s:
    if c != prev:
        prev = c
        answer += 10
    else:
        answer += 5
print(answer)