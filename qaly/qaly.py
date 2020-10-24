import sys

data = list(sys.stdin)
qaly = 0

for item in data[1:]:
        dat = item.split()
        qaly += float(dat[0])*float(dat[1])

print(f'{qaly}')
