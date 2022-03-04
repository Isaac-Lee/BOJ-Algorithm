a = int(input())
b = int(input()); c = int(input()); d = int(input())
p = int(input())
print(min(p*a, (b if p-c <= 0 else b+(p-c)*d)))