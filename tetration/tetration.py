import math

N = float(input())

delta = 10**-6

#f(a) = a**N-N

#f'(a) = math.log(a)*a**N + a**(N-1)

#f'(a) = N*a**(N-1)

prev = 0
a = N

while not( prev - delta < a < prev + delta):
    #print(a)
    prev = a
    #a = a - (a**N - N)/(math.log(a) * a**N + a**(N-1)) #newton step
    a = a - (a**N - N)/(N*a**(N-1)) # correct newton step
while not (1-delta < a/prev < 1 + delta):
    #print(a)
    prev = a
    #a = a -(a**N - N)/(math.log(a) * a**N + a**(N-1))
    a = a - (a**N - N)/(N*a**(N-1)) # correct newton step
print(a)
