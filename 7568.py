s = []
answer=[]
strng=""
for i in range(int(input())):
    s.append([int(k) for k in input().split()])
    answer.append(1)
for a in range(len(s)):
    for b in range(len(s)):
        if a == b:
            pass
        if s[a][0] < s[b][0] and s[a][1] < s[b][1]:
            answer[a] += 1
for c in answer:
    strng += str(c) + " "
print(strng)