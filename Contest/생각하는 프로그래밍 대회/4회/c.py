def gcd(a, b):
    while b != 0:
        r = a%b
        a=b
        b=r
    return a

def lcm(a, b):
    return a*b/gcd(a, b)


if __name__ == '__main__':
    nums = []
    answer = 1
    for i in range(int(input())):
        nums.append(int(input().split()[1]))
    for i in nums:
        answer = lcm(answer, i)
    print(1, int(answer))
