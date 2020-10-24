import sys

lst = ['Ball',None,None]

data = list(sys.stdin)[0]

for C in data:
    if C == 'A':
        temp = lst[0]
        lst[0] = lst[1]
        lst[1] = temp
    if C == 'B':
        temp = lst[1]
        lst[1] = lst[2]
        lst[2] = temp
    if C == 'C':
        temp = lst[0]
        lst[0] = lst[2]
        lst[2] = temp
print(1 if lst[0]=='Ball' else 2 if lst[1]=='Ball' else 3)
