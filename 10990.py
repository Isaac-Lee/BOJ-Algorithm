s = []

num = int(input())

for i in range(num):
    s.append('*'+' '*(2*i-1))

for i in range(num):
    s[i] = (" " *(num-i-1)+s[i])
    if i >= 1:
        s[i] = (s[i]+'*')

for i in range(num):
    print(s[i])