word = list(input())
d = list("CAMBRIDGE")
for c in d:
    if c in word:
        n = word.count(c)
        for i in range(n):
            word.remove(c)
for i in range(len(word)):
    print(word[i], end="")