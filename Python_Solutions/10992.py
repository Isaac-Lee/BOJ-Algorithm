n = int(input())
s=[]
for i in range(n):
    s.append(' '*(n-i-1)+'*')

for i in range(1,n-1):
    s[i] = s[i]+' '*(2*(i)-1)+'*'

s[n-1] = '*'*(2*n-1)

for i in range(n):
    print(s[i])