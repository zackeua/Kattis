
grid = [0,0,0,0]
grid[0] = list(map(int,input().split()))
grid[1] = list(map(int,input().split()))
grid[2] = list(map(int,input().split()))
grid[3] = list(map(int,input().split()))
dir = input()


if dir == "0":
    for row in grid:
        while 0 in row:
            row.remove(0)
        if len(row) > 1:
            if row[0] == row[1]:
                row.remove(row[0])
                row[0] = row[0]*2
                row.append(0)
        if len(row) > 2:
            if row[1] == row[2]:
                row.remove(row[1])
                row[1] = row[1]*2
                row.append(0)
        if len(row) > 3:
            if row[2] == row[3]:
                row.remove(row[2])
                row[2] = row[2]*2
                row.append(0)
        while len(row) < 4:
            row.append(0)

if dir == "2":
    for row in grid:
        while 0 in row:
            row.remove(0)
        row.reverse()
        if len(row) > 1:
            if row[0] == row[1]:
                row.remove(row[0])
                row[0] = row[0]*2
                row.append(0)
        if len(row) > 2:
            if row[1] == row[2]:
                row.remove(row[1])
                row[1] = row[1]*2
                row.append(0)
        if len(row) > 3:
            if row[2] == row[3]:
                row.remove(row[2])
                row[2] = row[2]*2
                row.append(0)
        while len(row) < 4:
            row.append(0)
        row.reverse()

if dir == "1":
    g = [[],[],[],[]]
    for row in grid:
        for i,elem in enumerate(row):
            g[i].append(elem)
    for row in g:
        while 0 in row:
            row.remove(0)
        if len(row) > 1:
            if row[0] == row[1]:
                row.remove(row[0])
                row[0] = row[0]*2
                row.append(0)
        if len(row) > 2:
            if row[1] == row[2]:
                row.remove(row[1])
                row[1] = row[1]*2
                row.append(0)
        if len(row) > 3:
            if row[2] == row[3]:
                row.remove(row[2])
                row[2] = row[2]*2
                row.append(0)
        while len(row) < 4:
            row.append(0)
    for row in range(4):
        for col in range(4):
            grid[row][col] = g[col][row]

if dir == "3":
    g = [[],[],[],[]]
    for row in grid:
        for i,elem in enumerate(row):
            g[i].append(elem)
    for row in g:
        while 0 in row:
            row.remove(0)
        row.reverse()
        if len(row) > 1:
            if row[0] == row[1]:
                row.remove(row[0])
                row[0] = row[0]*2
                row.append(0)
        if len(row) > 2:
            if row[1] == row[2]:
                row.remove(row[1])
                row[1] = row[1]*2
                row.append(0)
        if len(row) > 3:
            if row[2] == row[3]:
                row.remove(row[2])
                row[2] = row[2]*2
                row.append(0)
        while len(row) < 4:
            row.append(0)
        row.reverse()

    for row in range(4):
        for col in range(4):
            grid[row][col] = g[col][row]




for row in grid:
    for elem in row:
        print(elem, end=" ")
    print()
