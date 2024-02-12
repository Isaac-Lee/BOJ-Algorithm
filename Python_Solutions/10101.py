angle = []
for _ in range(3):
    angle.append(int(input()))
if sum(angle) != 180:
    print("Error")
elif angle.count(60) == 3:
    print("Equilateral")
elif len(set(angle)) == 2:
    print("Isosceles")
else:
    print("Scalene")