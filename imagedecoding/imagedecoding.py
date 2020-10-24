from sys import stdin

count = int(input())
c = 0

d = {'#':1, '.':-1}

p = {1:'#', -1:'.'}

while count != 0:
    sums = []
    for _ in range(count):
        row = input().split()
        s = 0
        c = d[row[0]]
        for n in row[1:]:
            s += int(n)
            for _ in range(int(n)):
                print(p[c], end="")
            c *= -1
        print()
        sums.append(s)
    if 1 in [sums[0] != nn for nn in sums]:
        print('Error decoding image')
    count = int(input())
    if count != 0:
        print()
