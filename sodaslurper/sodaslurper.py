e, f, c = list(map(int, input().split()))
total = 0
empty = e + f
new = -1
while new != 0:
        new = empty // c
        empty -= new * (c-1)
        total += new
print(total)