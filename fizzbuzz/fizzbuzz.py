import sys

data = list(sys.stdin)
dat = data[0].split()
X = int(dat[0])
Y = int(dat[1])
N = int(dat[2])

for i in range(1,N+1):
        out = ""

        if (i%X == 0):
                out += "Fizz"
        if (i%Y == 0):
                out += "Buzz"
        if (out == ""):
                out = str(i)
        print(out)