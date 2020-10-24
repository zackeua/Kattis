import sys


data = list(sys.stdin)

L, _ = list(map(int, data[0].split()))

total = 0
res = 0
for row in data[1:]:
    dir, count = row.split()
    count = int(count)
    if dir == 'enter':
        if total + count <= L:
            total += count
        else:
            res += 1
    else:
        total -= count
print(res)
