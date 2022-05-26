answer = 0
maximum = 0
minimum = 10001
n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)
maximum = rope[0]
for i in range(n):
    w = rope[i]
    answer = max(w*(i+1), maximum, answer)
print(answer)
