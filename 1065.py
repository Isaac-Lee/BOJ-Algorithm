n=int(input())
c=0
for i in range(1,n+1):
    num = str(i)
    if len(num) == 1 or len(num) == 2:
        c+=1
    elif len(num) >= 3:
        m = int(num[1]) - int(num[0])
        for j in range(1,len(num)):
            if (int(num[j]) - int(num[j-1])) != m:
                c -= 1
                break
        c += 1
print(c)