import sys

dat = list(sys.stdin)

data = dat[0].split()

H = int(data[0])

M = int(data[1])

time = H*60+M

time = (time - 45)%1440

hours = time//60
minutes = time%60

print(f'{hours} {minutes}')