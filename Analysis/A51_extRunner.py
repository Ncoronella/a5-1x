from A51_ext import A51_Stream
import sys
import time
from bitarray import bitarray
import random

random.seed(1)

def randomKey():
    return [random.randint(0, 1) for _ in range(64)]

start = time.perf_counter()

for i in range(200):
    key = randomKey()
    run = A51_Stream(key, f"Analysis/runs/{i}")
    run.tickXTimes(10**6)
    print(i)
tTime = ( time.perf_counter() - start)
print(f"200: {tTime:.6f} seconds")