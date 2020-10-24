#! /usr/bin/python3
import sys
 
for index, line in enumerate(sys.stdin):
    inp = line.split()
    if index == 0:
        numOfMachines = int(inp[0])
        nunOfItems = int(inp[1])
    elif index == 1:
        times = [int(i) for i in inp]
    else:
        time = sum(times) + max(times) * (nunOfItems - 1)
        print(time)
exit(0)