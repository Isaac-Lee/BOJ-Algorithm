for i in range(int(input())): # 테스트 케이스 동안
    xy = [int(k) for k in input().split()]
    x = xy[0]
    y = xy[1]
    # print(x,y)
    s = y-x
    i=1
    c = 0
    while(s != 0):
        if s >= i*2:
            if s == 1:
                i -= 1
            else:
                s -= i
                i += 1
                c += 1
        else:
            i-=1
    print(c)

'''
x에서 y로 갈때
처음과 끝 부분 1씩 감소
다음부터는 1 또는 2
반복.....

일단 미해결
'''