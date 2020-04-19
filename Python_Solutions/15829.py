def hash(str, len):
    index = 0
    for i in range(len):
        index += (ord(str[i]) - ord('a') + 1)*(31**i)
    return index % 1234567891


if __name__ == '__main__':
    len = int(input())
    s = list(input())
    print(hash(s, len))