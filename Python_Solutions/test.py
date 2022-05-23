for i in range(int(input())):
    n, x, y = map(int, input().split())
    s = (n*(n+1))//2
    possible = (s//(x+y) == s/(x+y))

    if not possible:
        print(f'Case #{i + 1}: IMPOSSIBLE')
    else:
        print(f'Case #{i + 1}: POSSIBLE')
        u = s // (x + y)
        Alan = u * x
        tmp = 0
        count = 0
        answer = []
        for k in range(n, 0, -1):
            if (tmp + k) <= Alan:
                tmp += k
                count += 1
                answer.append(k)
        print(count)
        print(*answer)
