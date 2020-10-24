def flightprob(flys, prob, day):
    ps = []
    for fly in flys:
        for f in flight[fly]:
            p = (day+1-s[f])/(t[f]-s[f])
            ps.append(prob*p)


N, M = list(map(int,input().split()))

s = [None]*N
t = [None]*N
flight = {}
day = 0
c = 0
for i in range(N):
    s[i], t[i] = list(map(int,input().split()))

for i in range(M):
    S, D = list(map(int,input().split()))
    if S in flight:
        flight[S].append(D)
    else:
        flight[S] = [D]


for f in flight[c]:
    prob = (c+2-s[f])/(t[f]-s[f])
    if prob < 0:
        prob = 0
    print(1-prob)
