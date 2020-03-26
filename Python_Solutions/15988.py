def make123(n):
    answer = [0, 1, 2, 4]
    if n < 4:
        return answer[n]
    for i in range(n-3):
        answer.append(answer[1]+answer[2]+answer[3])
        del answer[0]
    return answer[3]

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        k = int(input())
        print(make123(k)%1000000009)