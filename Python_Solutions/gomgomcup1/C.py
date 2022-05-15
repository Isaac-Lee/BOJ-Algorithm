n = int(input())
s = input()
cc = s.count("C")
answer = 0
if cc == n:
    answer = n
else:
    if cc == n - 1:
        answer = cc // 2
    else:
        if n % 2 == 1:
            answer = cc // (n - cc + 1)
        else:
            answer = cc // (n - cc)
    if cc%2 == 1:
        answer += 1
print(answer)
