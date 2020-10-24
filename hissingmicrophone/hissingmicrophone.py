import sys

s = list(sys.stdin)[0]

for i in range(1, len(s)):
    #print(i)
    if s[i-1] == 's' and s[i] == 's':
        print("hiss")
        break
else:
    print('no hiss')
