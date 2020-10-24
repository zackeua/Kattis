S = int(input())

print(f'{S}:')

for m in range(2,S):
    for n in [m-1, m]:
        count = 0
        while count < S:
            count += m+n
        if count == S or count - n == S:
            print(f'{m},{n}')
