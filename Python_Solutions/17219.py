n, m = map(int, input().split())
passwd = {}
for _ in range(n):
  addr, pw = input().split()
  passwd[addr] = pw
for _ in range(m):
  addr = input()
  print(passwd[addr])