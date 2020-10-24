
s, t, n = list(map(int,input().split()))
d = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
s += d[0]
for i in range(n):
    p = 0
    while c[i]*p < s:
        p += 1
    s = c[i]*p
    s += b[i]
    s += d[i+1]


print('yes' if s <= t else 'no')
