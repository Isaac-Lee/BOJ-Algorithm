for _ in range(int(input())):
    a,b = map(lambda x: int(x[::-1]), input().split())
    print(int(str(a+b)[::-1]))