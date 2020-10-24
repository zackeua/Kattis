maximum = int(input())
minimum = 0
i = 1

while i < 86:

    x = (maximum+minimum)//2
    #print(f'Day {i}, {6*i}')
    print(i*x, flush=True)
    answer = input()
    if answer == 'exact':
        exit(0)
    elif answer == 'less':
        maximum = x - 1
    else:
        minimum = x + 1
    x = (maximum + minimum)//2
    i += 1
