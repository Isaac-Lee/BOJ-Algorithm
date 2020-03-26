n = int(input())
s = 0
re = 1
b = 0
t = 0

for i in range(1, n+1):
    s += i
    if n <= s:
        re = i
        break
        
print(n, re, s)
if re == 1:
    b=1
    t=1        
elif re %2 == 0:
    b = 1+(s-n)
    t = re - (s-n)
else:
    b = re - (s-n)
    t = 1+(s-n)
print(str(t)+"/"+str(b))