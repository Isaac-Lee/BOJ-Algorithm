import sys

def makeBy(n):
    c1=1
    c2=2
    c3=0
    for i in range(3, n+1):
        c3 = c1 + c2
        c1, c2 = c2, c3
    print(c3%15746)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    makeBy(n)