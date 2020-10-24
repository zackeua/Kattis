import sys

data = list(sys.stdin)

iterations = int(data[0])

side = 2

for i in range(iterations):
        side = side + (side - 1)

print(side*side)