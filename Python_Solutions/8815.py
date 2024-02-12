answer = " ABCBCDCDADAB"
for i in range(int(input())):
    n = int(input())
    if n%12 == 0:
        print(answer[12])
    else:
        print(answer[n%12])