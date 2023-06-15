import sys
from rich import print
import time

messages = 0
ref = time.time()

for line in sys.stdin:   
    if time.time()-ref < 10:
        messages += 1
    else:
        print(ref, messages/10, "m/s")
        ref = time.time()
        messages = 0




