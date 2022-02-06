import sys
sys.setrecursionlimit(10**5)
n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

def tree(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    n = post_order[post_end]
    print(n, end=' ')
    i = in_order.index(n)
    l = i - in_start

    tree(in_start, i-1, post_start, post_start+l-1)
    tree(i+1, in_end, post_start+l, post_end-1)

tree(0,n-1,0,n-1)