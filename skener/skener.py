R, C, Z_R, Z_C = list(map(int, input().split()))

total = ''

numRows = 0

while numRows < R:
    row = input()
    tempRow = ''
    for e in row:
        tempRow += e*Z_C


    total += (tempRow + '\n')*Z_R
    numRows += 1

print(total)
