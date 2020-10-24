import re
from itertools import combinations_with_replacement



N, M = list(map(int, input().split()))
text = input()
text = text + text[0:M]


minDNA = 'z'*M
minScore = 0
print(text)
for i in range(N):
        s = text[i:i+M]
        #print(s)
        res = len(re.findall(s, text))
        print(f'{s}, {res}')
        if minScore <= res and minDNA > s:
                minScore = res
                minDNA = s

print(minDNA)
