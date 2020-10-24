n = int(input())
i = 0
T = []
D = []
while i < n:
        t, d = list(map(int, input().split()))
        T.append(t)
        D.append(d)
        i += 1
print(max([(D[i+1] - D[i])//(elem-T[i]) for i, elem in enumerate(T[1:])]))