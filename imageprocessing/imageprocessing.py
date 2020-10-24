H, W, N, M = list(map(int,input().split()))
c = 0
image = []
conv = []
out = [[0 for _ in range(W-M+1)] for _ in range(H-N+1)]
while c < H:
    image.append(list(map(int,input().split())))
    c += 1
c = 0
while c < N:
    l = list(map(int,input().split()))
    l.reverse()
    conv.insert(0,l)

    c += 1

for row in range(H-N+1):
    for col in range(W-M+1):
        sum = 0
        for i, convRow in enumerate(conv):
            for j, c in enumerate(convRow):
                sum += image[row+i][col+j]*c
        out[row][col] = sum

for row in out:
    for elem in row:
        print(elem, end=" ")
    print()
