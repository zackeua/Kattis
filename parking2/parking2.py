import sys

data = list(sys.stdin)


for row in data[2::2]:
    l = list(map(int,row.split()))
    print((max(l)-min(l))*2)
