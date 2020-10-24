import sys

data = list(sys.stdin)

area = 0
costPerArea = float(data[0])
lawns = int(data[1])
for i in range(lawns):
        dat = data[i+2].split()
        area = area + float(dat[0])*float(dat[1])

print(costPerArea*area)



