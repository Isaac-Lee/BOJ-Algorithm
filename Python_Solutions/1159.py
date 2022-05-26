count = [0]*26
for _ in range(int(input())):
    c = input()[0]
    count[ord(c)-97] += 1
isOk = False
for i in range(26):
    if count[i] >= 5:
        print(chr(i+97), end="")
        isOk = True
if not isOk:
    print("PREDAJA")
