import sys

data = list(sys.stdin)

N,B = data[0].split()
N = int(N)

######
sum = 0

for row in data[1:]:
    if 'A' in row:
        sum += 11
    elif 'K' in row:
        sum += 4
    elif 'Q' in row:
        sum += 3
    elif 'J' in row and B in row:
        sum += 20
    elif 'J' in row:
        sum += 2
    elif 'T' in row:
        sum += 10
    elif '9' in row and B in row:
        sum += 14

print(sum)
