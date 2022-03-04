import math
w, h = map(int, input().split())
print(h+w-math.sqrt(h*h+w*w))
