N = 123456 * 2 + 1
sieve = [True, False] + [True]* (N-1)
for i in range(1, int(N**0.5)+1):
    if sieve[i]:
        sieve[i * 2::i] = [False] * ((N - i) // i)

i = int(input())
while i != 0:
    print(len([x for x in range(i+1, 2*i+1) if sieve[x]]))
    i = int(input())