import sys

check = 0
dist = 0
out = ""
for index, item in enumerate(sys.stdin):
        if (check == index):
                check = index + int(item) + 1
                if (index != 0):
                        out = out + f'{dist} miles\n'
                dist = 0
                time = 0
        else:
                data = item.split()
                dist = dist + int(data[0]) * (int(data[1]) - time)
                time = int(data[1])

print(out)