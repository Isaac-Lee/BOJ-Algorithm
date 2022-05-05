for _ in range(int(input())):
    t = int(input())
    print(t//25, end=" ")
    t = t%25
    print(t//10, end=" ")
    t = t % 10
    print(t//5, end=" ")
    t = t % 5
    print(t//1)
