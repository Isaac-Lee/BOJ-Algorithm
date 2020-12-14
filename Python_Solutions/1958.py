def lca(s1, s2, len1, len2):
    LCA = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                LCA[i][j] = LCA[i - 1][j - 1] + 1
            else:
                LCA[i][j] = max(LCA[i - 1][j], LCA[i][j - 1])

    answer = ""
    x = len1
    y = len2
    current = LCA[-1][-1]
    while LCA[x][y] != 0:
        if LCA[x][y - 1] == current - 1 and LCA[x - 1][y] == current - 1:
            answer = s1[x - 1] + answer
            current -= 1
            x -= 1
            y -= 1
        else:
            if LCA[x - 1][y] > LCA[x][y - 1]:
                x -= 1
            else:
                y -= 1
    return answer


s1 = input()
s2 = input()
s3 = input()

len1 = len(s1)
len2 = len(s2)
len3 = len(s3)

s12 = lca(s1, s2, len1, len2)
len12 = len(s12)

print(len(lca(s3, s12, len3, len12)))