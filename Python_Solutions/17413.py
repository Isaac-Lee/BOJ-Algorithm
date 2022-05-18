from collections import deque

S = input()
word = deque()
tagFlag = False
for c in S:
    if c == "<":
        while word:
            print(word.pop(), end="")
        tagFlag = True
        print(c, end="")
    elif c == ">":
        tagFlag = False
        print(c, end="")
    elif c == " ":
        while word:
            print(word.pop(), end="")
        print(" ", end="")
    else:
        if tagFlag:
            print(c, end="")
        else:
            word.append(c)
while word:
    print(word.pop(), end="")
