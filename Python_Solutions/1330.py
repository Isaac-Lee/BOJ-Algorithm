n = input()
nl = n.split(" ")
a = int(nl[0])
b = int(nl[1])

if a<b:
    print('<')
elif a > b:
    print('>')
else:
    print('==')
