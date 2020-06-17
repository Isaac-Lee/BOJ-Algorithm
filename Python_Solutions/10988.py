word = list(input())
i = 0
j = len(word)-1
isPal = True
while i < j:
    if word[i] == word[j]:
        i += 1
        j -= 1
    else:
        isPal = False
        break
if isPal:
    print(1)
else:
    print(0)