def s1(N):
    return int(N*(N+1)/2)

def s2(N):
    return N*N

def s3(N):
    return N*(N+1)

N = int(input())
i = 0

while i < N:
    m, n = list(map(int, input().split()))
    print(f'{m} {s1(n)} {s2(n)} {s3(n)}')
    i += 1
