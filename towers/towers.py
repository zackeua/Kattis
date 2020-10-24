import sys
import math

def lg(list):
    res = 0
    for i,elem in enumerate(list,0):
        temp = elem
        for j in range(len(list)-i):
            temp = math.log(temp)
        res += temp
    return res


def lg2(list):
    if len(list) == 1:
        return math.log2(list[0])
    else:
        return math.log2(list[-1]*lg2(list[:-1]))

def lg3(list,n):
    if len(list) == 1:
        return math.log2(list[0]), n-1
    else:
        t, n = lg3(list[:-1],n-1)
        res = math.log2(list[-1]*t)
    if res != 0:
        for i in range(n):
            print(res)
            res = math.log2(res)
    return res,0


d = {}

data = list(sys.stdin)

for row in data[1:]:
    l = list(map(int, row.split('^')))
    while(len(l) < 100):
        l.append(1)
    t = lg2(l)
    if t in d:
        d[t].append(row)
    else:
        d[t] = [row]

keys = list(d.keys())
keys.sort()
s = f'Case 1:\n'
for k in keys:
    for e in d[k]:
        s += f'{e} {k}\n'
        #print(e)
    #print(d[k])
print(s)
