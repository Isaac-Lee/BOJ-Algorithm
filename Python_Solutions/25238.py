a, b = map(int, input().split())
if a < 100:
    print(1)
elif a-(a*(b/100)) < 100:
    print(1)
else:
    print(0)