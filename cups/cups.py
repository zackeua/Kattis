import sys

data = list(sys.stdin)[1:]

res = []

for row in data:
    A,B = row.split()
    try:
        N = int(A)
        res.append((N,B))
    except Exception as e:
        N = 2*int(B)
        res.append((N,A))

res.sort(key=lambda n : n[0])

for row in res:
    print(row[1])
