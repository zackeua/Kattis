import sys

dat = list(sys.stdin)

data = dat[0].split()
first = int(data[0][::-1])
second = int(data[1][::-1])
if (first < second):
        print(second)
else:
        print(first)