import sys
from math import ceil

data = []
for index, line in enumerate(sys.stdin):
        if (index == 0):
                inp = line.split()
                numberOfReqests = int(inp[0])
                maxRequests = int(inp[1])
        else:
                data.append(int(line))

amounts = []
for i in range(numberOfReqests):
        #print(data[i:])
        amounts.append(len([1 for item in data[i:] if item < data[i]+1000]))
print(ceil(max(amounts)/maxRequests))
