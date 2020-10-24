import sys

data = list(sys.stdin)

stat = [0,0,0,0]
string = data[0]
for char in string[0:-1]:
        if (char == '_'):
                stat[0] += 1
        elif (ord('a') <= ord(char) <=ord('z')):
                stat[1] += 1
        elif (ord('A') <= ord(char) <=ord('Z')):
                stat[2] += 1
        else:
                stat[3] += 1
print(f'{stat[0]/len(string[0:-1])}\n{stat[1]/len(string[0:-1])}\n{stat[2]/len(string[0:-1])}\n{stat[3]/len(string[0:-1])}')