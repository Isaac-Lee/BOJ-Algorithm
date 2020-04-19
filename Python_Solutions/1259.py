def isPal(number):
    while len(number) >= 0:
        if len(number) == 1 or len(number) == 0:
            return "yes"
        if number[0] == number[-1]:
            del number[0]
            del number[-1]
            continue
        else:
            return "no"


while True:
    n = input()
    num = []
    for i in range(len(n)):
        num.append(n[i])
    if n[0] == '0':
        break
    print(isPal(num))
