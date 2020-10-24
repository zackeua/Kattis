N  = int(input())
M = int(input())

extra = 0
while (M//N * N + extra < M):
    extra += 1
for i in range(N):
    if i < extra:
        s = "*"*(M//N+1)
        print(s)
    else:
        s = "*"*(M//N)
        print(s)
