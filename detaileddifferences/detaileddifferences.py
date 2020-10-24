import sys


data = list(sys.stdin)

for i in range(int(data[0])):
    print(data[1+i*2])
    print(data[2+i*2])
    s = ""
    for j in range(len(data[1+i*2])-1):
        if data[1+i*2][j] == data[2+i*2][j]:
            s += "."
        else:
            s += "*"
    print(s)
