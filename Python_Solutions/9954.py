expr = '[A-Za-z]'
while True:
    s = input()
    diff = ord(s[-1])-ord('A')
    if s == "#":
        break
    for c in s[:-1]:
        if c.isalpha():
            if c.isupper():
                print(chr(((ord(c)-65-diff)+26)%26+65), end="")
            elif c.islower():
                print(chr(((ord(c)-97-diff)+26)%26+97), end="")
        else:
            print(c, end='')
    print()