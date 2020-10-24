N,Q = list(map(int,input().split()))
companies = list(map(int,input().split()))

def distance(A,B):
    a = int(A)-1
    b = int(B)-1
    res = companies[a] - companies[b]
    if res < 0:
        return -res
    return res


c = 0


while c < Q:
    T, A, B = input().split()
    if T == "1":
        companies[int(A)-1] = int(B)
    else:
        print(distance(A,B))
    c += 1
