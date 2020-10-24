import sys

l = list(sys.stdin)


for row in l[1:]:
    K,N = list(map(int,row.split()))
    tot = N
    for i in range(1,N+1):
        tot += i
    print(f'{K} {tot}')
