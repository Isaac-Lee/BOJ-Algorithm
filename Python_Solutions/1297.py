D, H, W = map(int, input().split())
C = (H*H+W*W)**(1/2)
print(int((D/C)*H), int((D/C)*W))