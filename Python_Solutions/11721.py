s = list(input())
for i in range(len(s)):
    print(s[i], end="")
    if (i+1)%10 == 0:
        print("")