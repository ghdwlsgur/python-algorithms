
# 유쿨리드 기하학 3.14 * r ** r
# 택시 기하학 r * 2r

import sys
from math import pi
r = int(sys.stdin.readline())
print("{:.6f}".format(pi * (r ** 2)))
print("{:.6f}".format(r * (2 * r)))
