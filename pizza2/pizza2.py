import sys

data = list(sys.stdin)
dat = data[0].split()
R = int(dat[0])
C = int(dat[1])

percent = 10*(R-C)/R

#percent = percent * percent
print(percent*percent)



