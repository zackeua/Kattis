import sys
import math

dat = list(sys.stdin)
data = dat[0].split()

print(math.ceil(int(data[0])/math.sin(math.pi*int(data[1])/180)))