answer = []
for i in range(1,6):
    agnt = input()
    if "FBI" in agnt:
        answer.append(i)
if len(answer) >0:
    for n in answer:
        print(n, end=" ")
else:
    print("HE GOT AWAY!")