import sys

data = list(sys.stdin)[1:]

for row in data:
    a,b,c = list(map(float,row.split()))
    if a+b == c or a*b==c or a-b==c or b-a==c or a/b==c or b/a==c:
        print('Possible')
    else:
        print('Impossible')
