for _ in range(int(input())):
    string = "{0:b}".format(int(input()))[::-1]
    result = []
    offset = -1
    while True:
        try:
            offset = string.index('1', offset + 1)
        except ValueError:
            print(*result)
            break
        result.append(offset)
