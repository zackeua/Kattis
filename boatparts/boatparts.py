P, N = list(map(int, input().split()))
prev_words = []
i = 0
printed = False
while i < N:
    word = input()
    if word not in prev_words:
        prev_words.append(word)
    if len(prev_words) == P and not printed:
        print(i+1)
        printed = True
    i += 1
if not printed:
    print('paradox avoided')
