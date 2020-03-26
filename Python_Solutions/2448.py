import math

s = ['  *   ', ' * *  ', '***** ']


def make_fractal(shift):
    c = len(s)
    for i in range(c):
        s.append(s[i] + s[i])
        s[i] = ("   " * shift + s[i] + "   " * shift)


n = int(input())
k = int(math.log(int(n / 3), 2))
for i in range(k):
    make_fractal(int(pow(2, i)))
for i in range(n):
    print(s[i])