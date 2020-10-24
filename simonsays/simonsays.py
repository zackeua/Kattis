import sys

data = list(sys.stdin)

for row in data[1:]:
    if len(row) > 10 and row[0:10] == 'Simon says':
        print(row[10:])
