s = input()
re = 0
for c in s:
    if c == "A" or c == "B" or c == "C":
        re += 3
    elif c == "D" or c == "E" or c == "F":
        re += 4
    elif c == "G" or c == "H" or c == "I":
        re += 5
    elif c == "J" or c == "K" or c == "L":
        re += 6
    elif c == "M" or c == "N" or c == "O":
        re += 7
    elif c == "P" or c == "Q" or c == "R" or c == "S":
        re += 8
    elif c == "T" or c == "U" or c == "V":
        re += 9
    elif c == "W" or c == "X" or c == "Y" or c == "Z":
        re += 10
print(re)