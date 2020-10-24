import sys

s = ""
data = int(input())
res = 0
while data != 0:
    res = res * 2
    if data % 2 == 1:
        #s = "1" + s
        data = data - 1
        res = res + 1
    #else:
        #s = "0" + s
    data = data/2

#for c in s[::-1]:
#    data = data * 2
#    if c == '1':
#        data += 1
print(res)
#print(int(data))
