from math import pi
a = {" ":0, "'":1, "A":2,
     "B":3, "C":4, "D":5,
     "E":6, "F":7, "G":8,
     "H":9, "I":10, "J":11,
     "K":12, "L":13, "M":14,
     "N":15, "O":16, "P":17,
     "Q":18, "R":19, "S":20,
     "T":21, "U":22, "V":23,
     "W":24, "X":25, "Y":26,
     "Z":27}

d = pi*60/28/15

N = int(input())
c = 0

while c < N:
        s = input()
        score = 0
        for i in range(len(s)-1):
                diff = a[s[i]] - a[s[i+1]]
                score += min([diff%len(a), (-diff)%len(a)])
        score *= d
        score += len(s)
        print(score)
        c += 1
