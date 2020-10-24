import sys
import math

inp = list(sys.stdin)
data = [item.split() for item in inp]

out = [[float(item[0]), int(item[1]), int(item[2])] for item in data]

for i in range(len(data)):
        if (out[i][0] != 0):
                print(f'{math.pi*out[i][0]*out[i][0]} {out[i][0]*out[i][0]*4*out[i][2]/out[i][1]}')
        