N = int(input())
Q = input()
A = "ABC"
B = "BABC"
G = "CCAABB"

a = 0
b = 0
g = 0
for i in range(N):
    if Q[i] == A[i%len(A)]:
        a += 1
    if Q[i] == B[i%len(B)]:
        b += 1
    if Q[i] == G[i%len(G)]:
        g += 1

biggest = max([a,b,g])
print(biggest)
if biggest == a:
    print("Adrian")
if biggest == b:
    print("Bruno")
if biggest == g:
    print("Goran")
