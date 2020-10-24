#! /usr/bin/python3
import sys
 
for line in sys.stdin:
    c = float(line)
    if c <= 1:
        print(c*c/4)
    else:
        print(0.25)
exit(0)