import sys

data = list(map(int,list(sys.stdin)[0].split()))[1]

print('possible' if data%2==0 else 'impossible')
