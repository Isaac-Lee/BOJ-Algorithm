n = int(input())
for i in range(n):
    string = ""
    num = input().split()
    for j in range(0, len(num[1])):
        string += num[1][j]*int(num[0])
    print(string)