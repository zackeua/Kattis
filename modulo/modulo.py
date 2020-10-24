import sys

data = list(sys.stdin)
dat = [int(i) for i in data]
modded = [0]*42
result = 0
for i in dat:
    modded[i%42]+=1

for i in modded:
    if i > 0:
        result+=1
print(f'{result}')
