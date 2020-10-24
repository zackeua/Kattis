import sys


for i, row in enumerate(list(sys.stdin), 1):
    x,y,r = list(map(float,row.split()))
    z = complex(0,0)
    c = complex(x,y)
    count = 0
    while abs(z) <= 2 and count < r:
        z = z**2 + c
        count += 1

    if abs(z) > 2:
        print(f'Case {i}: OUT')
    else:
        print(f'Case {i}: In')
