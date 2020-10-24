import sys


data = list(map(int,list(sys.stdin)[0].split()))
data.sort()
print(data[0]*data[2])
