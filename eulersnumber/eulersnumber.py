n = int(input())


f = {0:1,1:1}

def factorial(n):
    if n in f:
        return f[n]
    f[n] = n*factorial(n-1)
    return f[n]

e = 0

for i in range(n+1):
    e += 1/factorial(i)
print(e)
