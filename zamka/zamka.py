import sys

L,D,X = list(map(int,list(sys.stdin)))

N = D+1
M = L-1

for i in range(L,D+1):
    s = str(i)
    if X == sum(list(map(int,s))) and N == D+1:
        N = i


for i in range(D,L-1,-1):
    s = str(i)
    if X == sum(list(map(int,s))) and M == L-1:
        M = i

print(N)
print(M)
