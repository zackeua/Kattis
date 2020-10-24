n = int(input())

while n  != 0:
        i = 0
        L1 = []
        L2 = []
        d = {}

        while i < n:
                L1.append(int(input()))
                i += 1
        i = 0
        L1Sorted = L1.copy()
        L1Sorted.sort()

        while i < n:
                L2.append(int(input()))
                i += 1
        L2.sort()
        
        for a, b in zip(L1Sorted, L2):
                d[a] = b
        
        for a in L1:
                print(d[a])
        print()
        n = int(input())