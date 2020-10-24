from math import tan, pi
N = int(input())
i = 0

for _ in range(N):
        n, l, d, g = list(map(int, input().split()))
        p = n*l
        a = l/(2*tan(pi/n))
        A = p*a/2 + n*l*d*g + pi*(d*g)**2
        print(A)

"""
2
3 8 1 1
4 5 2 2

"""