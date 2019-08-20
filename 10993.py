from builtins import range

n = int(input())

width = 1
height = 1

four = 4
two = 2
for i in range(n - 1):
    width += four
    four *= 2

    height += two
    two *= 2

star = []
for i in range(height):
    for j in range(width):
        star.append([False])


def drawStar(s, e, hlen, wlen, n):

    mid = int((s + s + wlen) // 2)
    left = s
    right = s + wlen


    if n % 2 == 1:
        inL = mid
        inR = mid
        for i in range(e, e + hlen):
            for j in range(inL, inR + 1):
                if i == e or i == e + hlen - 1 or j == inL or j == inR:
                    star[j] = True
                else:
                    continue
            inL -= 1
            inR += 1

    else:
        inL = left
        inR = right
        for i in range(e, e + hlen):
            for j in range(inL, inR + 1):
                if i == e or i == e + hlen - 1 or j == inL or j == inR - 1:
                    star[j] = True
                else:
                    continue
            inL += 1
            inR -= 1

    moveR = s + 2 ** (n - 1)
    if n % 2 == 1:
        drawStar(moveR, e + hlen//2, hlen//2, wlen - n**2, n - 1)
    else:
        drawStar(moveR, e + 1, hlen//2, wlen - n**2, n - 1)


drawStar(0, 0, height, width, n)

stars = ''
if n%2 ==1:
    k=1
    for i in range(height):
        for j in range(width//2+k):
            if star[i][j]:
                stars += '*'
            else:
                stars += ' '
        stars += '\n'
        k+=1

else:
    k = 0
    for i in range(height):
        for j in range(width // 2 + k):
            if star[i][j]:
                stars += '*'
            else:
                stars += ' '
        stars += '\n'
        k+=1

print(stars)