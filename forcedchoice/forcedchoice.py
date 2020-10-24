N, P, S = list(map(int, input().split()))

i = 0

while i < S:
        labels = list(map(int, input().split()))
        print('KEEP' if P in labels[1:] else 'REMOVE')
        i += 1