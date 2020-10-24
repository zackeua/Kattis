import sys
import itertools
data = [int(item) for item in list(sys.stdin)]
over = sum(data) - 100

#print(f'{over}')

for i, j in itertools.combinations(range(len(data)), 2):
        if (data[i] + data[j] == over):
                I = i
                J = j
                break

for k in range(len(data)):
        if (k != I and k != J):
                print(f'{data[k]}')