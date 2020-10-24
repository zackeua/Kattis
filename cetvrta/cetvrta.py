import sys

X = []
Y = []
for item in sys.stdin:
        data = item.split()
        X.append(int(data[0]))
        Y.append(int(data[1]))
if (X[0] == X[1]):
        x = X[2]
elif (X[0] == X[2]):
        x = X[1]
else:
        x = X[0]

if (Y[0] == Y[1]):
        y = Y[2]
elif (Y[0] == Y[2]):
        y = Y[1]
else:
        y = Y[0]
print(f'{x} {y}')