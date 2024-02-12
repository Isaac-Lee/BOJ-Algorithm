s_h,s_m,s_s = map(int, input().split()[::2])
e_h,e_m,e_s = map(int, input().split()[::2])

s_time = s_h*3600+s_m*60+s_s
e_time = e_h*3600+e_m*60+e_s

if e_time < s_time:
    e_time += 24*3600

print(e_time-s_time)