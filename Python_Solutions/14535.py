Case = 1
T = int(input())
month = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
while T > 0:
    n = [0 for _ in range(13)]
    for _ in range(T):
        date = input()
        n[int(date[3:5])] += 1
    print(f'Case #{Case}:')
    for i in range(1, 13):
        print(f'{month[i]}:'+'*'*n[i])
    Case += 1
    T = int(input())