s = input()
if len(s) > 3:
    print(20)
elif len(s) > 2:
    if s.index('0')==1:
        print(10 + int(s[2]))
    else:
        print(10 + int(s[0]))
else:
    print(int(s[0]) + int(s[1]))