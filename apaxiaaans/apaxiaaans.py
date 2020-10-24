s = list(input())

i = 0
while i < len(s)-1:
        while i != len(s)-1 and s[i] == s[i+1]:
                s = s[0:i] + s[i+1:]
        i += 1

res = ''

for c in s:
        res += c

print(res)