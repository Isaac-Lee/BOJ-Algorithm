n = int(input())
if n == 0:
    print("divide by zero")
    exit(0)
l = list(map(int, input().split()))
if sum(l) == 0:
    print("divide by zero")
    exit(0)
print(f'{1.0:.2f}')