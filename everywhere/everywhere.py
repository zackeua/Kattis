import sys

l = list(sys.stdin)
count = 0
for i, elem in enumerate(l[1:]):
    if count == i:
        count = i+int(elem)+1
        if i != 0:
            print(len(d))
        d = {}
    else:
        d[elem] = 1
        #print(elem)
    #print(f'{i}\t{elem}')
print(len(d))
