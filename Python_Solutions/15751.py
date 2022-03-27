a,b,x,y = map(int,input().split())
if a>b: a,b = b,a
if x>y: x,y = y,x
print(min(abs(a - b), abs(a-x)+abs(b-y)))