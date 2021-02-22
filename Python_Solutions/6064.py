def our_year(m, n, x, y):
    year = x
    while year < m*n:
        if year%n == 0:
            temp_year = n
        else:
            temp_year = year%n
        if temp_year == y:
            return year
        year += m
    return -1


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(our_year(m, n, x, y))