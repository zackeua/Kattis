
ul = 8
ur = 8

ll = 8
lr = 8

n = int(input())
i = 0
while i < n:
    inp = input()
    blue = inp[-1] == 'b'
    if '+' == inp[0]:
        ul -= 1
        if blue == True:
            ul = -1
    elif '-' == inp[0]:
        ll -= 1
        if blue == True:
            ll = -1
    elif '+' == inp[1]:
        ur -= 1
        if blue == True:
            ur = -1
    else:
        lr -= 1
        if blue == True:
            lr = -1
    i += 1
#print(f'ul {ul}\nll {ll}\nur {ur}\nlr {lr}\n')
if (ul <= 0 or ll <= 0) and (ur <= 0 or lr <= 0):
    print(2)
elif ul <= 0 or ll <= 0:
    print(1)
else:
    print(0)
