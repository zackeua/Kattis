from math import sqrt
T = int(input())

i = 0
while i < T:
    n, e = list(map(int,input().split()))
    prod = [None, None]
    for p in range(2, int(sqrt(n))+1):
        if n%p==0:
            prod = [p-1, n//p -1]
    phi = prod[0]*prod[1]
    d = 1
    while d*e%phi != 1:
        d += 1
    print(d)
    i += 1
