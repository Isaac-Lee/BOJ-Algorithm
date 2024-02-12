import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        k = int(input())
        print(make123(k)%1000000009)