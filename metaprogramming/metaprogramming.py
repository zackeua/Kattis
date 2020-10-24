from sys import stdin

def less(a, b):
    return a < b

def eq(a, b):
    return a == b

def more(a, b):
    return a > b

data = list(stdin)

d = {}
ops = {'<':less, '=': eq , '>':more}

for row in data:
    if 'define' in row:
        op, val, var = row.split()
        val = int(val)
        d[var] = val
    else:
        op, var1, comp, var2 = row.split()
        if var1 not in d or var2 not in d:
            print('undefined')
        else:
            print('true' if ops[comp](d[var1], d[var2]) else 'false')
