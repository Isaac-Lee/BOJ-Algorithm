import sys

def findMax(n):
    answer = []
    for i in range(n):
        k = list(map(int, input().split()))
        if i == 0:
            answer = k
            continue
        elif i == 1:
            k[0] += answer[0]
            k[1] += answer[0]
            answer = k
        elif i >= 2:
            k[0] += answer[0]
            for j in range(1, i):
                k[j] += max(answer[j-1], answer[j])
            k[i] += answer[i-1]
            answer = k
    return max(answer)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(findMax(n))