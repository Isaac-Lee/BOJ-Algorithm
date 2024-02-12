A = 0
A += int(input())*3
A += int(input())*2
A += int(input())*1

B = 0
B += int(input())*3
B += int(input())*2
B += int(input())*1

if A == B:
    print('T')
else:
    if A > B:
        print("A")
    else:
        print("B")