import sys
from math import factorial

data = list(map(int,list(sys.stdin)[1:]))


for d in data:
    print(str(factorial(d))[-1])
