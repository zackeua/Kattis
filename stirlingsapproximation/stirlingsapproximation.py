from sys import stdin
from math import sqrt, pi, log, lgamma, exp

a = log(sqrt(2*pi))

def stirling(n):

    total = lgamma(n+1) - (0.5+n)*log(n) + n - a

    return exp(total)

 
for elem in list(stdin)[:-1]:
    print(stirling(int(elem)))
