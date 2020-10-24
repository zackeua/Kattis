n = int(input())
num = 1
while n != 0:
    names = []
    for _ in range(n):
        names.append(input())

    print(f'SET {num}')
    if n%2==1:
        for i in range(0,n,2):
            print(names[i])
        for i in range(n-2, -1, -2):
            print(names[i])
    else:
        for i in range(0,n,2):
            print(names[i])
        for i in range(n-1, -1, -2):
            print(names[i])

    n = int(input())
    num += 1
