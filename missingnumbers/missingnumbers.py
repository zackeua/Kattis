N = int(input())

l = [None]*(201)
i = 0

while i < N:
    n = int(input())
    l[n] = n
    i += 1

flag = 1
for i in range(1,n+1):
    if l[i] == None:
        print(i)
        flag = 0

if flag:
    print('good job')
