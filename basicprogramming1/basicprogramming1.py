import sys
import statistics

inp = list(sys.stdin)
data = [int(item) for item in inp[0].split()]
N = data[0]
t = data[1]
A = [int(item) for item in inp[1].split()]

if (t == 1):
        print(f'7')
elif (t == 2):
        if (A[0] > A[1]):
                print(f'Bigger')
        elif (A[0] == A[1]):
                print(f'Equal')
        else:
                print(f'Smaller')
elif (t == 3):
        print(f'{statistics.median(A[0:3])}')
elif (t == 4):
        print(f'{sum(A)}')
elif (t == 5):
        print(f'{sum([item for item in A if item%2 == 0])}')
elif (t == 6):
        for item in A:
                print(f'{chr(item%26 + 97)}',end='')
        print()
elif (t == 7):
        i = 0
        count = 0
        while (count < N + 1):
                i = A[i]
                if (i == N-1):
                        print(f'Done')
                        break
                elif (i >= N):
                        print(f'Out')
                        break
                elif (count == N):
                        print(f'Cyclic')
                count += 1