n = input()
s1 = input().split()
s2 = input().split()

len1 = len(s1)
len2 = len(s2)

LCA = [[0] * (len2+1) for _ in range(len1+1)]
for i in range(1, len1+1):
    for j in range(1, len2+1):
        if s1[i-1] == s2[j-1]:
            LCA[i][j] = LCA[i-1][j-1] + 1
        else:
            LCA[i][j] = max(LCA[i-1][j], LCA[i][j-1])
print(LCA[-1][-1])