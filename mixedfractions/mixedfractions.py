inp = input()

while inp != '0 0':
        a, b = list(map(int, inp.split(' ')))
        print(f'{a//b} {a%b} / {b}')
        inp = input()
