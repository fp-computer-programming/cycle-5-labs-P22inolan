# Author: IBN (AMDG) 10/25/2021

import math
import time

start_1 = time.perf_counter()
math.pow(2, 2)
end_1 = time.perf_counter()

final1 = end_1 - start_1
print(final1)

start_2 = time.perf_counter()
(2 ** 2)
end_2 = time.perf_counter()

final2 = end_2 - start_2
print(final2)
print(final1 - final2)
