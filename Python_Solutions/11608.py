import heapq
heap = []
s = input()
n = len(set(s))
for i in range(26):
    c = s.count(chr(97+i))
    if c > 0:
        heapq.heappush(heap, c)
if n > 2:
    result = 0
    for _ in range(-(2-n)):
        result += heapq.heappop(heap)
    print(result)
else:
    print(0)