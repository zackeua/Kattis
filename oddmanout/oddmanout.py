N = int(input())
i = 0
while i < N:
    G = int(input())
    j = 0
    d = {}
    l = list(map(int,input().split()))
    for elem in l:
        if elem in d:
            d[elem] += 1
        else:
            d[elem] = 1
    for key in d.keys():
        if d[key] == 1:
            print(f'Case #{i+1}: {key}')

    i += 1
