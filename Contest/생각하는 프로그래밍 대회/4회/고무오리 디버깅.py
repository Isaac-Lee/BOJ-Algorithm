s = input()
problems = 0
while True:
    s = input()
    if s == "고무오리":
        if problems == 0:
            problems += 2
        else:
            problems -= 1
            continue
    elif s == "문제":
        problems += 1
        continue
    elif s == "고무오리 디버깅 끝":
        break
if problems > 0:
    print("힝구")
else:
    print("고무오리야 사랑해")