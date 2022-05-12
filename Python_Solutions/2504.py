from collections import deque
s = input()
stack = deque()
answer = 0
tmp = 1

for i, c in enumerate(s):
    if c == '(' or c == '[':
        stack.append(c)
        tmp *= (2 if c == '(' else 3)
    else:
        if stack and c == ')'  and stack[-1] == '(':
            if s[i-1] == '(':
                answer += tmp
            stack.pop()
            tmp //= 2
        elif stack and c == ']' and stack[-1] == '[':
            if s[i-1] == '[':
                answer += tmp
            stack.pop()
            tmp //= 3
        else:
            answer = 0
            break

if stack:
    print(0)
else:
    print(answer)