import sys

uniCount = [None]*12
data = list(sys.stdin)[1:]

s = ""
count = 0
for row in data:
    uni, name = row.split()
    if count < 12 and not uni in uniCount:
        uniCount[count] = uni
        s += row
        count += 1

print(s)
