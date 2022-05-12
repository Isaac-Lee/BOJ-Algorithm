while 1:
    try:
        count = [0 for _ in range(4)]
        for c in input():
            if c.isalpha():
                if c.islower():
                    count[0] += 1
                elif c.isupper():
                    count[1] += 1
            elif c.isdigit():
                count[2] += 1
            elif c.isspace():
                count[3] += 1
        print(*count)
    except EOFError:
        break