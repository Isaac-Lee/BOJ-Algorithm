s = input()
for c in s:
    if not c.isalpha():
        print(c, end="")
    else:
        if c.isupper():
            print(chr((ord(c)-65+13)%26+65), end="")
        else:
            print(chr((ord(c)-97+13)%26+97), end="")
