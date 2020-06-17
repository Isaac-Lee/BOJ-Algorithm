cnt = 0
for i in range(8):
    line = input()
    for j in range(8):
        if i%2 == 1:
            if j%2 == 1:
                if line[j] == "F":
                    cnt+=1
        else:
            if j%2 == 0:
                if line[j] == "F":
                    cnt+=1
print(cnt)