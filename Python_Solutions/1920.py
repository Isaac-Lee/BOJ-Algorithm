n = input()
num = list(map(int, input().split()))
k = int(input())
for i in list(map(int, input().split())):
    if i in num:
        print(1)
    else:
        print(0)