def eatChar(s):
        vovels = 'aeiou'
        if s[0] in vovels:
                return s[0], s[3:]
        else:
                return s[0], s[1:]

s = input()

ans = ''
while s is not '':
        temp, s = eatChar(s)
        ans += temp
print(ans)