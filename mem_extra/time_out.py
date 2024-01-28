import time

with open('mem_extra/timing.txt', 'r') as f:
    t0 = f.readlines()[-1].replace("\\\\\n", "")

with open('mem_extra/timing.txt', 'a') as f:
    t1 = time.time()
    f.write(str(t1) + "\\\\\n")
    f.write(str(t1-float(t0)) + "\n\n")
