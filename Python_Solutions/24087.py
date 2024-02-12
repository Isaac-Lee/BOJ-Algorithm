s=int(input());a=int(input());b=int(input());
if s <= a:
    print(250)
    exit(0)
c = (s-a)//b
if (s-a)%b > 0:
    c += 1
print(c*100+250)