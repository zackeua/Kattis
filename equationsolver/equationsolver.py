import sys

def det(A):
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    res = 0
    for i, elem in enumerate(A[0]):
        mini = [[e for j,e in enumerate(row) if i!=j] for row in A[1:]]
        d = elem*det(mini)
        if i%2==0:
            res += d
        else:
            res -= d
    return res

def LU(A):
    n = len(A)
    L = [[ 0 for x in range(n)] for y in range(n)]
    U = [[ 0 for x in range(n)] for y in range(n)]

    for i in range(n):

        for k in range(i,n):
            sum = 0
            for j in range(i):
                sum += (L[i][j] * U[j][k])
            U[i][k] = A[i][k] - sum

        for k in range(i,n):
            if (i==k):
                L[i][k] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (L[k][j] * U[j][i])
                L[k][i] = (A[k][i] - sum)/U[i][i]

    return L,U

def mul(M1,M2):
    if len(M1[0]) != len(M2):
        raise Exception(f'Dimensions of matrices are wrong.')
    res = []
    N = len(M1)
    M = len(M2[0])
    L = len(M2)
    for i in range(N):
        temp = []
        for j in range(M):
            sum = 0
            for k in range(L):
                sum += (M1[i][k] * M2[k][j])
            temp.append(sum)
        res.append(temp)

def forward_sub(L,y):
    if len(y) != len(L[0]):
        raise Exception(f'Dimensions of L and y are wrong.')
    l = len(L)
    x = [0 for i in range(l)]
    for i in range(l):
        if i == 0:
            x[i] = y[i]/L[i][i]
        else:
            sum = 0
            for j in range(i):
                sum += (L[i][j] * y[j])
            x[i] = (y[i] - sum)/L[i][i]
    return x

def backward_sub(U,y):
    if len(y) != len(U[0]):
        raise Exception(f'Dimensions of U and y are wrong.')
        print('error!!!')
    l = len(U)
    x = [0 for i in range(l)]
    for i in range(l-1,0-1,-1):
        if i == l-1:
            x[i] = y[i]/U[i][i]
        else:
            sum = 0
            for j in range(i+1,l):
                sum += (U[i][j] * y[j])
            x[i] = (y[i] - sum)/U[i][i]
    return x

def solve(A,B):
    L,U = LU(A)
    if U != []:
        b = forward_sub(L,B)
        x = backward_sub(U,b)
    else:
        x = L
    return x

data = list(sys.stdin)
count = 0
for i, row in enumerate(data):
    l = row.split()
    if i == count:
        l = int(l[0])
        count = i+l+2
        if i != 0:
            if det(A) != 0:
                x = solve(A,B)
                for elem in x:
                    print(f'{elem} ',end = '')
                print()
            else:
                printed = True
                for i in range(len(A)):
                    for j in range(len(A)):
                        if printed and i != j and B[j] != 0:
                            c = B[i]/B[j]
                            if A[i] == [ci*c for ci in A[j]]:
                                    print('multiple')
                                    printed = False
                        elif i != j and printed and B[i] == B[j] and A[i] == A[j]:
                            print('multiple')
                            printed = False
                if printed:
                    print('inconsistent')
        A = []
    elif i < count - 1:
        A.append(list(map(float,l)))
    else:
        B = list(map(float,l))
