
from math import factorial
def catalan(n):
    return factorial(2*n)//(int(factorial(n))*int(factorial(n+1)))
    '''
    res = 1
    for k in range(2,n+1):
        res *= (n+k)/k
    return int(round(res))
    '''

q = int(input())
i = 0

while i < q:
    print(catalan(int(input())))
    i += 1
