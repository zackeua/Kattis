import sys
import math

data = list(sys.stdin)[:-1]

for row in data:
    D, V = map(int,row.split())
    print((D**3 - 6*V/math.pi)**(1/3))
