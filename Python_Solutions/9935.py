from collections import deque

s = input()
word = input()
stack = deque()
l = len(word)
for c in s:
    stack.appendleft(c)
    if c == word[-1]:
        isWord = True
        for i in range(l):
            if len(stack) < l:
                isWord = False
                break
            if word[l - i - 1] != stack[i]:
                isWord = False
        if isWord:
            for _ in range(l):
                stack.popleft()

if not stack:
    print("FRULA")
else:
    for _ in range(len(stack)):
        print(stack.pop(), end="")
