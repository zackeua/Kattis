import sys

inp = list(sys.stdin)
data = [int(item) for item in inp[1].split()]

total = 0

for item in data:
        if (item < 0):
                total += 1

print(f'{total}')