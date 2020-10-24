N = int(input())

c = 0

while c < N:
    C, D, H, M = input().split()
    D = int(D)
    H = int(H)
    M = int(M)
    t = 60*H+M
    if C == "B":
        t -= D
    else:
        t += D
    H = t//60
    M = t - H*60
    print(f'{H%24} {M}')
    c += 1
