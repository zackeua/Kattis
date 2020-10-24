import sys

data = list(sys.stdin)
dat = [int(i) for i in data]
result = ""
for i in range(1, dat[0]+1):
    result += f'{dat[i]} is {"even" if dat[i]%2 == 0 else "odd"}\n'
print(result)
