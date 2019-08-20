n = int(input())
reN = n

width = 0
height = 0

width += 4 * (n - 1)
if n >= 2:
    height += 6 + (4 * (n - 2))

stars = []
for i in range(height + 1):
    stars.append([])
    for j in range(width + 1):
        stars[i] += ' '

top = 0
bot = height+1
left = 0
right = width+1


def leftDown(seq):
    global top, left, bot, right, reN
    if seq < 0:
        return
    if seq < reN:
        bot -= 2
    for i in range(top, bot):
        for j in range(left, right):
            if i == top or j == left:
                stars[i][j] = '*'
    if seq < reN:
        right -= 2
    rightUp(seq)


def rightUp(seq):
    global top, left, bot, right
    top += 2
    if seq < 0:
        return
    for i in range(top, bot):
        for j in range(left, right):
            if i == bot-1 or j == right-1:
                stars[i][j] = '*'

    left += 2
    leftDown(seq - 1)


leftDown(n)


re =[]
for i in range(height+1):
    re.append([''])
    for chr in stars[i]:
        if i == 1:
            re[i][0] = '*'
        else:
            re[i][0] += chr
    print(re[i][0])
