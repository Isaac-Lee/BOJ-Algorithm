n = list(input())
n.sort(reverse = True)
answer = ""
for c in n:
    answer += c
print(answer)