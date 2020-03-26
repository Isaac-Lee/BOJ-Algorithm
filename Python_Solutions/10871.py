import sys
n=list(map(int, input().split()))[0]
numlist = list(map(int, input().split()))
nstring = ''
for i in numlist:
    if i < n:
        nstring += '%d' % i
        nstring += ' '
print(nstring)