# a, b, c = map(int, input().split())
# print(pow(a, b, c))

a, b, c = map(int, input().split())

def div(a, n):
    if n == 1:
        return a % c
    elif n == 2:
        return a * a
    else:
        tmp = div(a, n//2)
        if n%2 == 0:
            return tmp*tmp % c
        else:
            return tmp*tmp*a % c

print(div(a, b))