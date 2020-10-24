lower = 1
upper = 1000

i = 0
while i < 10:
    guess = (upper + lower)//2
    print(guess, flush=True)
    inp = input()
    if inp == 'correct':
        break
    elif inp == 'lower':
        upper = guess - 1
    else:
        lower = guess + 1
    i += 1
