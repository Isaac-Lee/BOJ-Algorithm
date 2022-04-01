import time
start = time.time()
a=1
for i in range(100000000):
    a = a+1

print("time :", time.time() - start)