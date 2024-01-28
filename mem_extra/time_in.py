import time
import sys

with open('mem_extra/timing.txt', 'a') as f:
    f.write(' '.join(sys.argv[1:]).replace("_", "\\_") + "\n")
    f.write(str(time.time()) + "\\\\\n")
