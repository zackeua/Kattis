import sys

data = list(sys.stdin)
dat = data[0].split()

R1 = int(dat[0])
S = int(dat[1])

R2 = S*2 - R1
print(R2)