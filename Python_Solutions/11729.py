c=0
sec = []
def HanoiTowerMove(num, fro, by, to):
    if num == 1:
        print(fro, to)
    else:
        HanoiTowerMove(num-1, fro, to, by)
        print(fro, to)
        HanoiTowerMove(num-1, by, fro, to)

n = int(input())
HanoiTowerMove(n,1,2,3)