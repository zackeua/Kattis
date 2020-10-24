def SSN(b, n):
        i = 0
        res = 0
        while b**i < n:
                i += 1
        while i !=-1:
                res += (n // (b**i))**2
                n = n %(b**i)
                i -= 1
        return res

P = int(input())
p = 0

while p < P:
        i, b, n = list(map(int, input().split()))
        print(f'{i} {SSN(b, n)}')
        p += 1