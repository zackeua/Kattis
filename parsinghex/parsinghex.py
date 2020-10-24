from sys import stdin
import re


def toDecimal(hex):
    d = {'0':0, '1':1, '2':2, '3':3, '4':4,
    '5':5, '6':6, '7':7, '8':8, '9':9,
    'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    res = 0
    for c in hex.lower():
        res *= 16
        res += d[c]
    return res

data = list(stdin)

pattern = re.compile("0[xX][0-9a-fA-F]{1,8}.")

for row in data:
    result = pattern.findall(row[:-1]+'u')
    for elem in result:
        print(f'{elem[:-1]} {toDecimal(elem[2:-1])}')
