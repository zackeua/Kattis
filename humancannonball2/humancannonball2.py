import sys
from math import sin, cos, pi
data = list(sys.stdin)[1:]

for row in data:
    v0, theta, x1, h1, h2 = list(map(float,row.split()))
    height = x1*sin(pi*theta/180)/cos(pi*theta/180)-0.5*9.81*(x1/(v0*cos(pi*theta/180)))**2
    #print(h1+1)
    #print(height)
    #print(h2-1)
    if h1 + 1 < height < h2 - 1:
        print('Safe')
    else:
        print('Not safe')
