N,K = list(map(int,input().split()))

c = 0

data = [[0 for _ in range(N)] for _ in range(3)]
max = [[] for _ in range(3)]
while c < N:
    data[0][c], data[1][c], data[2][c] = list(map(int,input().split()))
    c += 1
