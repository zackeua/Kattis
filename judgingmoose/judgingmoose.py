import sys

l,r = list(map(int,list(sys.stdin)[0].split()))
if l == r:
    if l == 0:
        print('Not a moose')
    else:
        print(f'Even {2*r}')
else:
    print(f'Odd {2*max([l,r])}')
