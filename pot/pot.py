import sys

data = []
X = 0
for index, line in enumerate(sys.stdin):
        if (index == 0):
                N = int(line[0])
        else:
                data.append(line)

for i in range(N):
        X += int(data[i][0:-2])**int(data[i][-2])

print(X)