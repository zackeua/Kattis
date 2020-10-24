import sys

G, S, C = list(map(int,list(sys.stdin)[0].split()))

total = 3*G + 2*S + C

result = ''

if total >= 8:
    result += 'Province'
elif total >= 5:
    result += 'Duchy'
elif total >= 2:
    result += 'Estate'

if result != '':
    result += ' or '

if total >= 6:
    result += 'Gold'
elif total >= 3:
    result += 'Silver'
else:
    result += 'Copper'

print(result)
