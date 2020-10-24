T = int(input())
iter = 0
while iter < T:
    q1 = int(input())
    p1 = list(map(int,input().split()))
    q2 = int(input())
    p2 = list(map(int,input().split()))
    degree = q1+q2
    p = [0]*(degree+1)
    for i, a in enumerate(p1):
        for j, b in enumerate(p2):
            p[i+j] += a*b
    print(degree)
    for c in p:
        print(c, end=' ')
    print()
    iter += 1
