from collections import defaultdict

n = int(input())
book = defaultdict(int)
for _ in range(n):
    title = input()
    book[title] += 1
count = max(book.values())
answer = []
for t in book:
    if book[t] == count:
        answer.append(t)
answer.sort()
print(answer[0])
