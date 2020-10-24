import sys


l = list(sys.stdin)[1:]

for row in l:
    b,p = list(map(float,row.split()))
    print(f'{60*(b-1)/p:.4f} {60*b/p:.4f} {60*(b+1)/p:.4f}')
