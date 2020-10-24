import sys

data = list(sys.stdin)

for row in data[1:]:
    print(len(row)-1)
