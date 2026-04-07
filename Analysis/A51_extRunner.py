from A51_ext import A51_Stream
import sys
import time
from bitarray import bitarray
import random

random.seed(1)

def randomKey():
    return [random.randint(0, 1) for _ in range(64)]

start = time.perf_counter()
#outpath = f"Analysis/runs/{i}"
outpath = "Combined output"

for i in range(200):
    key = randomKey()
    run = A51_Stream(key, outpath)
    run.tickXTimes(10**6)
tTime = ( time.perf_counter() - start)
print(f"1000: {tTime:.6f} seconds")