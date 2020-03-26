def make123(n):
    if n < 4:
        for i in range(1, n+1):
            count[i] = sum(count[:i])+1
    else:
        for i in range(1, 4):
            count[i] = sum(count[:i])+1
        for i in range(4, n + 1):
            count[i] = sum(count[:i])
    return count[n]

def find123(n, begin, end):
    if n == 0:
        return 0
    f = count[n-1]
    s = count[n-2] + count[n-1]
    e = count[n]

    if n >= 1 and (begin < k <= begin + f):
        answer.append(1)
        return find123(n-1, begin, begin + f)
    elif n >= 2 and (begin + f < k <= begin + s):
        answer.append(2)
        return find123(n-2, begin + f, begin + s)
    elif n >= 3 and (begin + s < k <= begin + e):
        answer.append(3)
        return find123(n-3, begin + s, begin + e)

if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    count = [0] * (n + 1)
    answer = []
    answerStr = ""
    maxK = make123(n)
    find123(n, 0, count[n])

    print(answer)

    if maxK < k:
        print(-1)
        exit(0)

    for i in range(len(answer)):
        answerStr += "%d" %answer[i]
        if i < len(answer)-1:
            answerStr += "+"