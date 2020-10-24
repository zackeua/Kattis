from random import randint
#print(randint(0,1))
print(1)
num = int(input())
while num < 99:
    if num%10 == 8:
        num += 1
    elif num%10 == 7:
        num += 2
    elif num%10 == 6:
        pass # never here
    elif num%10 == 5:
        num += 1
    elif num%10 == 4:
        num += 2
    elif num%10 == 3:
        pass # never here
    elif num%10 == 2:
        num += 1
    elif num%10 == 1:
        num += 2
    elif num%10 == 0:
        num += 2
    print(f'{num}')
    if num < 99:
        num = int(input())
