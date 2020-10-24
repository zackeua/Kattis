import sys

data = list(sys.stdin)

W = int(data[0])

A = 0

for row in data[2:]:
    w,l = list(map(int,row.split()))
    A += w*l
print(A//W)
