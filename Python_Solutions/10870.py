def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return factorial(n-1) + factorial(n-2)

num = int(input())
print(factorial(num))