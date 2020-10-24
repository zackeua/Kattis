Y, P = input().split()

if Y[-1] == 'e':
    print(f'{Y}x{P}')
elif Y[-1] in 'aiou':
    print(f'{Y[:-1]}ex{P}')
elif Y[-2:] == 'ex':
    print(f'{Y}{P}')
else:
    print(f'{Y}ex{P}')
