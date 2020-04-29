from sys import *

n, m = map(int, stdin.readline().split())
pokemon = []
for i in range(n):
    pokemon.append(stdin.readline())
for i in range(m):
    n = stdin.readline()
    try:
        stdout.write(pokemon[int(n)-1])
    except:
        stdout.write(str(pokemon.index(n)+1)+"\n")