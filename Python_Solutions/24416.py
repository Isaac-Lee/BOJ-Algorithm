def fib(n):
    f1 = f2 = 1
    for i in range(2, n):
        tmp = f2%1000000007
        f2 += f1%1000000007
        f1 = tmp
    return f2%1000000007

def dp(n):
    return n-2

if __name__ == '__main__':
    n = int(input())
    print(fib(n), dp(n))
