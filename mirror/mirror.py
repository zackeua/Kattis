import sys

data = list(sys.stdin)

c = 0
cc = 1
for i, row in enumerate(data[1:]):
    if i == c:
        R,C = list(map(int,row.split()))
        c = i + R + 1
        if i != 0:
            print(f'Test {cc}')
            print(A)
            cc += 1
        A = ''
    else:
        A = row[::-1] + A
print(f'Test {cc}')
print(A)
