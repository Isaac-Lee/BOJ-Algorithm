from collections import deque

operator = {'+', '-', '*', '/'}

def eval(expr, op, num):
    if expr:
        a = expr.pop()
        if a in operator:
            int_a = eval(expr, a, num)
        else:
            int_a = num[ord(a) - ord('A')]
        b = expr.pop()
        if b in operator:
            int_b = eval(expr, b, num)
        else:
            int_b = num[ord(b) - ord('A')]
        match op:
            case '+':
                return int_b + int_a
            case '-':
                return int_b - int_a
            case '*':
                return int_b * int_a
            case '/':
                return int_b / int_a

if __name__ == '__main__':
    N = int(input())
    expr = input()
    num = []
    for _ in range(N):
        num.append(int(input()))

    expr = deque(expr)

    op = expr.pop()
    print("{:.2f}".format(eval(expr, op, num)))
