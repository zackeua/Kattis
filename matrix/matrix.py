import sys

data = list(sys.stdin)

m = []
c = 0
for row in data:
    if row != "\n":
        m.append(list(map(int,row.split())))
    else:
        c += 1
        print(f'Case {c}:')
        det = m[0][0]*m[1][1]-m[0][1]*m[1][0]
        print(f'{m[1][1]//det} {-m[0][1]//det}\n{-m[1][0]//det} {m[0][0]//det}')
        m = []
