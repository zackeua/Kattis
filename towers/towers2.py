import sys


def power(list):
    if len(list) == 1:
        return list[0]
    if list[0] == 1:
        return 1
    if list[0] == 0:
        return 0
    res = 1
    p = power(list[1:])
    while p > 0:
        if p % 2 == 0:
            p = p // 2
            list[0] = list[0] * list[0]
        else:
            p = p - 1
            res = res * list[0]

    return res

d = {}

data = list(sys.stdin)

for row in data[1:]:
    l = list(map(int, row.split('^')))
    t = power(l)
    if t in d:
        d[t].append(row)
    else:
        d[t] = [row]

keys = list(d.keys())
keys.sort()
s = f'Case 1:\n'
for k in keys:
    for e in d[k]:
        s += f'{e}\n'
        #print(e)
    #print(d[k])
print(s)
