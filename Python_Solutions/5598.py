answer = ""
for c in input():
    asc = ord(c)
    if asc < ord("D"):
        answer += chr(ord("Z")-(ord("C")-asc))
    else:
        answer += chr(ord(c)-3)
print(answer)