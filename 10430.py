n_s = input()
n_l = n_s.split(" ")
A = int(n_l[0])
B = int(n_l[1])
C = int(n_l[2])

print((A + B) % C)
print((A % C + B % C) % C)

print((A * B) % C)
print((A % C * B % C) % C)