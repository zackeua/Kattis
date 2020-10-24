S = input()

S1 = S[:len(S)//2]
S1 = [c for c in S1]
S2 = S[len(S)//2:]
S2 = [c for c in S2]
#print(S1, len(S1))
#print(S2, len(S2))

rot1 = 0
for c in S1:
    rot1 += ord(c) - ord('A')
#print(rot1)
for i in range(len(S1)):
    S1[i] = chr(ord('A') + (ord(S1[i])+rot1)%(ord('Z')-ord('A')+1))
#print(S1)

rot2 = 0
for c in S2:
    rot2 += ord(c) - ord('A')
#print(rot1)
for i in range(len(S2)):
    S2[i] = chr(ord('A') + (ord(S2[i])+rot2)%(ord('Z')-ord('A')+1))
#print(S2)


for c1, c2 in zip(S1, S2):
    print(chr(ord('A') + (ord(c1) + ord(c2))%(ord('Z')-ord('A')+1)),end="")
