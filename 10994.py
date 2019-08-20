n = int(input())

width = 0

width = width + 4*(n - 1)

stars = []  ## 별 그리는 배열

## width*width 개의 칸을 빈칸으로 체우기
for i in range(width+1):
    stars.append([])
    for j in range(width+1):
        stars[i] += ' '


def darwBox(s, width, n): # (시작지점, 변의 길이, 안쪽에서 몇번째 사각형인지)
    left = s
    right = s + width

    top = s
    bot = s + width

    if n < 0:
        return

    ## 사각형 그리기
    for i in range(top, bot):
        for j in range(left, right):
            if i == top or i == bot-1 or j == left or j == right-1: #맨 위/아래, 양옆에 별로 체우기
                stars[i][j] = '*'
            else:
                stars[i][j] = ' '

    darwBox(top + 2, width - 4, n - 1)  ## 재귀


darwBox(0, width+1, n)

# 한 줄의 문자열로 만들기 / 출력까지
re =[]
for i in range(width+1):
    re.append([''])
    for chr in stars[i]:
        re[i][0] += chr
    print(re[i][0])
