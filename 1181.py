word =[]
for _ in range(int(input())):
    word.append(input())
wordset = set(word)
word = list(wordset)
word = sorted(word, key= lambda x: (len(x), x))
for w in word:
    print(w)