from collections import deque

center_expr = deque(input())
stack = deque()
back_expr = ''

while center_expr:
    n = center_expr.popleft()
    if n.isalpha():
        back_expr += n
    elif n == '(':
        stack.append(n)
    elif n == ')':
        while stack and stack[-1] != '(':
            back_expr += stack.pop()
        stack.pop()
    elif n == '*' or n == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            back_expr += stack.pop()
        stack.append(n)
    elif n == '+' or n == '-':
        while stack and stack[-1] != '(':
            back_expr += stack.pop()
        stack.append(n)

while stack:
    op = stack.pop()
    if op != '(' and op != ')':
        back_expr += op

print(back_expr)
