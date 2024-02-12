for _ in range(3):
    on_h, on_m, on_s, off_h, off_m, off_s = map(int, input().split())
    on = (on_h*3600) + (on_m * 60) + on_s
    off = (off_h*3600) + (off_m * 60) + off_s
    work = off-on
    h = work//3600
    m = (work % 3600)//60
    s = (work % 3600) % 60
    print(h, m, s)