n=int(input());l=list(map(int,input().split()));l.sort();a=[]
while len(l)>0:a.append(l.pop(0)+l.pop())
print(min(a))