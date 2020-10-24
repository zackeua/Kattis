import sys

data = []
for index, line in enumerate(sys.stdin):
        if (index == 0):
                inp = line.split()
                N = int(inp[0])
                W = int(inp[1])
                H = int(inp[2])
        else:
                data.append(int(line))

maxLength = (W*W + H*H)**(1/2)

for i in range(N):
        if (data[i] <= maxLength):
                print("DA")
        else:
                print("NE")