n = int(input())
cor = list(map(int, input().split()))

set_cor = set(cor)
sorted_cor = sorted(list(set_cor))

compress_cor = {}

for i in range(len(sorted_cor)):
    compress_cor[sorted_cor[i]] = i

answer = ""
for i in range(n):
    answer += str(compress_cor[cor[i]]) + " "

print(answer)