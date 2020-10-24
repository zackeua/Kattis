import sys

class Dog:
    """docstring for Dog."""

    def __init__(self, on, off):
        self.on = on
        self.off = off
    def isAgressive(self,t):
        clock = 0
        res = True
        while clock < t:
            if res:
                clock += self.on
            else:
                clock += self.off
            res = not res
        return not res



data = list(sys.stdin)

A,B,C,D = list(map(int,data[0].split()))
P,M,G = list(map(int,data[1].split()))
dog1 = Dog(A,B)
dog2 = Dog(C,D)

Pd1 = dog1.isAgressive(P)
Pd2 = dog2.isAgressive(P)

Md1 = dog1.isAgressive(M)
Md2 = dog2.isAgressive(M)

Gd1 = dog1.isAgressive(G)
Gd2 = dog2.isAgressive(G)

Pt = Pd1 + Pd2
Mt = Md1 + Md2
Gt = Gd1 + Gd2

if Pt == 2:
    print('both')
elif Pt == 1:
    print('one')
else:
    print('none')

if Mt == 2:
    print('both')
elif Mt == 1:
    print('one')
else:
    print('none')


if Gt == 2:
    print('both')
elif Gt == 1:
    print('one')
else:
    print('none')
