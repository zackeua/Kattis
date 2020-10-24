import sys

data = list(sys.stdin)
p = True
for i, row in enumerate(data,1):
    if "FBI" in row:
        print(i, end=" ")
        p = False
if p:
    print("HE GOT AWAY!")
