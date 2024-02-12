from collections import deque

def eval(op, expr, num):
    a = expr.pop()
    if a in operator:
        eval(op, expr, num)
    int_a = num[ord(a) - ord('A')]
    b = expr.pop()
    if b in operator:
        eval(op, expr, num)
    int_b = num[ord(b) - ord('A')]
    match op:
        case '+':
            return int_a + int_b
        case '-':
            return int_a - int_b
        case '*':
            return int_a * int_b
        case '/':
            return int_a / int_b

operator = {'+', '-', '*', '/'}

N = int(input())
expr = deque(input())
num = [int(input()) for _ in range(N)]



print("{:.2f}".format(eval(expr, op, num)))
