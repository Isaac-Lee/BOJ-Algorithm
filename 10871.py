import sys
nlist=[int(k) for k in sys.stdin.readline().split()]
numlist = [int(k) for k in sys.stdin.readline().split()]

nstring = ''

for i in numlist:
    if i < nlist[1]:
        nstring += '%d' % i
        nstring += ' '
print(nstring)