a,b,c = map(int,input().split())
if a==b==c:
    print("*")
elif a!=b==c:
    print("A")
elif a==c!=b:
    print("B")
elif a==b!=c:
    print("C")