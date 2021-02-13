def compress(x1, y1, n):
    color = img[x1][y1]
    if n == 1:
        return color
    for x in range(x1, x1+n):
        for y in range(y1, y1+n):
            current_color = img[x][y]
            if color != current_color:
                color = "("+compress(x1, y1, n//2)
                color += compress(x1, y1+n//2, n//2)
                color += compress(x1+n//2, y1, n//2)
                color += compress(x1+n//2, y1+n//2, n//2)+")"
                return color
    return color


if __name__ == '__main__':
    n = int(input())
    img = []
    for _ in range(n):
        img.append([c for c in input()])
    print(compress(0, 0, n))