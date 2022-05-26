for c in input():
    if c.isupper():
        print(c.lower(), end="")
    if c.islower():
        print(c.upper(), end="")