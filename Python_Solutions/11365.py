while True:
    s = input()
    if s == "END":
        break
    for c in reversed(s):
        print(c, end="")
    print()