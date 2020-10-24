def toList(s):
    return [c for c in s]

def toStr(L):
    s = ''
    for c in L:
        s += c
    if s == '':
        s = 'YODA'
    else:
        s = int(s)
    return s

def compare(N, M):
    for i in range(min([len(N), len(M)])):
        if N[i] < M[i]:
            N[i] = None
        elif N[i] > M[i]:
            M[i] = None
    while None in N:
        N.remove(None)
    while None in M:
        M.remove(None)

N = toList(input()[::-1])
M = toList(input()[::-1])

#N = N[::-1]
#M = M[::-1]

#N = toList(N)
#M = toList(M)

compare(N,M)

#N = toStr(N[::-1])
#M = toStr(M[::-1])

#N = toStr(N)
#M = toStr(M)

#print(N)
#print(M)
print(toStr(N[::-1]))
print(toStr(M[::-1]))
