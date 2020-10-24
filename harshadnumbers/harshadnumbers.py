n = int(input())

p = True

while p:
    if n%sum(map(int, str(n))) == 0:
        print(n)
        p = False
    n = n+1
