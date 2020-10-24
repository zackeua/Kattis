def minimum(w, g, h, r):
    return ((g-h)**2 + w**2)**(1/2)


def func(w, g, h, r, a):
    return ((g-r)**2 + (a)**2)**(1/2) + ((h-r)**2 + (w-a)**2)**(1/2)

def deriv(w, g, h, r, a):
    return a/((g-r)**2 + a**2)**(1/2) - (w-a)/((h-r)**2 + (w-a)**2)**(1/2)

def maximum(w, g, h, r):
    a_prev = 0
    a = w/2
    tempVal = func(w, g, h, r, a_prev)
    val = func(w, g, h, r, a)
    count = 0
    while deriv(w, g, h, r, a) != 0 and  not (-10**(-6) < func(w, g, h, r, a_prev) - func(w, g, h, r, a) < 10**(-6)):
        #print('hör')
        #print(f'{func(w, g, h, r, a)}')
        a_prev = a
        a = a - (1-count/4000)*func(w, g, h, r, a)/deriv(w, g, h, r, a)
        tempVal = val
        val = func(w, g, h, r, a)
        count += 1
    return func(w, g, h, r, a)

'''
def maximum(w, g, h, r):
    if g == h:
        a = w/2
    else:
        a = w*(h-r)**2/((g-r)**2 - (h-r)**2)
    return ((g-r)**2 + (w-a)**2)**(1/2) + ((h-r)**2 + (a)**2)**(1/2)
'''

N = int(input())

i = 0

while i < N:
    w, g, h, r = list(map(int,input().split()))
    print(f'{minimum(w, g, h, r)} {maximum(w, g, h, r)}')
    i += 1
