import sys

data = list(sys.stdin)[1:]

for row in data:
    if '+' in row:
        a,b = list(map(int,row.split('+')))
        print(a+b)
    else:
        print('skipped')
