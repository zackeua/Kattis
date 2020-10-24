from sys import stdin
R,C = list(map(int,input().split()))


data = list(stdin)
#print(R)
#print(C)
#print(data)
#print(data[0][0:2])
'''
for row in range(R):
    for col in range(C):
        print(data[row][col],end="")
    print()
'''
R = R - 1
C = C - 1

count = 0
for row in range(R):
    for col in range(C):
        if data[row][col:col+2] in ['..'] and data[row+1][col:col+2] in ['..']:
            count += 1
print(count)

count = 0
for row in range(R):
    for col in range(C):
        if data[row][col:col+2] in ['.X','X.'] and data[row+1][col:col+2] in ['..']:
            count += 1
        elif data[row][col:col+2] in ['..'] and data[row+1][col:col+2] in ['.X','X.']:
            count += 1
print(count)

count = 0
for row in range(R):
    for col in range(C):
        if data[row][col:col+2] in ['XX'] and data[row+1][col:col+2] in ['..']:
            count += 1
        elif data[row][col:col+2] in ['..'] and data[row+1][col:col+2] in ['XX']:
            count += 1
        elif data[row][col:col+2] in ['.X','X.'] and data[row+1][col:col+2] in ['.X','X.']:
            count += 1
print(count)

count = 0
for row in range(R):
    for col in range(C):
        if data[row][col:col+2] in ['XX'] and data[row+1][col:col+2] in ['.X','X.']:
            count += 1
        elif data[row][col:col+2] in ['.X', 'X.'] and data[row+1][col:col+2] in ['XX']:
            count += 1
print(count)

count = 0
for row in range(R):
    for col in range(C):
        if data[row][col:col+2] in ['XX'] and data[row+1][col:col+2] in ['XX']:
            count += 1
print(count)
