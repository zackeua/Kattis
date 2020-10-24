import sys


data = list(sys.stdin)[1:]


for text in data:
    l = int((len(text)-1)**(1/2))
    #for i in range(l):
    #    print(f'{text[i*l:i*l+l]}')
    for j in range(l-1,0-1,-1):
        for i in range(l):
            print(f'{text[i*l+j]}',end="")
    print()
