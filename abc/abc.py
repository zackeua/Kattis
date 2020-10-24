import sys

data = list(sys.stdin)
dat = [int(item) for item in data[0].split()]

A = min(dat)
C = max(dat)

for i in range(3):
   if (A < dat[i] < C):
      B = dat[i]
      
for i in range(3):
   if (data[1][i] == 'A'):
      print(f'{A} ',end="")
   elif (data[1][i] == 'B'):
      print(f'{B} ',end="")
   else:
      print(f'{C} ',end="")
print()