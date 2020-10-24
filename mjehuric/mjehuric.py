def printList(L):
    for elem in L:
        print(elem, end=' ')
    print()

def swap(L, i):
    if L[i] > L[i+1]:
        L[i], L[i+1] = L[i+1], L[i]
        printList(L)

def sorted(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

L = list(map(int, input().split()))

i = 0
while not sorted(L):
    swap(L,i)
    i += 1
    if i >= 4:
        i = 0
