word = input()
answer = 0
for c in word:
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        answer += 1
print(answer)