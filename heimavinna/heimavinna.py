import sys

data = list(sys.stdin)

data = data[0]

total = 0

if ';' in data:
    data = data.split(';')
else:
    data = [data]

for val in data:
    if '-' in val:
        low, high = val.split('-')
        total += (int(high) - int(low)) + 1
    else:
        total += 1

print(total)
