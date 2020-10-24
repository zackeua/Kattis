import sys

N,M = list(map(int,list(sys.stdin)[0].split()))

d = {i:0 for i in range(2,N+M+1)}
#print(d)
tot = 0
for n in range(1,N+1):
    for m in range(1,M+1):
        d[n+m] += 1
        tot += 1

#print(d)
#print(tot)

max = 0
for i in range(2,N+M+1):
    if max < d[i]:
        max = d[i]
        maxList = [i]
    elif max == d[i]:
        maxList.append(i)
for e in maxList:
    print(e)
