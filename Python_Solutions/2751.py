import sys

answer=[]
for _ in range(int(sys.stdin.readline())):
    answer.append(int(sys.stdin.readline()))
answer.sort()
for n in answer:
    sys.stdout.write(str(n)+"\n")