import sys

data = []
for index, line in enumerate(sys.stdin):
        if (index == 0):
                X = int(line)
        elif (index == 1):
                N = int(line)
        else:
                data.append(int(line))
available = (N+1)*X 
for i in range(N):
        available -= data[i]
print(available)