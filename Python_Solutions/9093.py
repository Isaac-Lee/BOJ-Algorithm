for _ in range(int(input())):
    s = input().split()
    for w in s:
        print(w[::-1], end=" ")
    print()