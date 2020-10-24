import sys
from math import ceil,floor

A,I = list(map(int,list(sys.stdin)[0].split()))

res = 0

while I != ceil(res/A):
    res += 1

print(res)
