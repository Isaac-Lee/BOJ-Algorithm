A,a,B,b,P = map(int,input().split())
if A+B <= P:
    print('Yes')
elif B <= a and A <= P:
    print('Yes')
elif A <= b and B <= P:
    print('Yes')
else:
    print('No')