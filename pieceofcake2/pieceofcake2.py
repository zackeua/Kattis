import sys

data = list(sys.stdin)
dat = [int(i) for i in data[0].split()]

volume = [dat[1]*dat[2], (dat[0]-dat[1])*dat[2], dat[1]*(dat[0]-dat[2]), (dat[0]-dat[1])*(dat[0]-dat[2])]
print(f'{4*max(volume)}')
