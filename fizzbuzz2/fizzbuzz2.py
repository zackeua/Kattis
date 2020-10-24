N, M = list(map(int, input().split()))

i = 0

total = []
while i < N:
        score = 0
        row = list(input().split())
        for index, elem in enumerate(row):
                if (index+1) % 15 == 0:
                        score += elem == 'fizzbuzz'
                elif (index+1) % 3 == 0:
                        score += elem == 'fizz'
                elif (index+1) % 5 == 0:
                        score += elem == 'buzz'
                else:
                        try:
                                score += elem == str(index+1)
                        except:
                                pass
        total.append(score)
        i += 1

maxindex = 0

for i in range(len(total)):
        if total[i] > total[maxindex]:
                maxindex = i 
print(maxindex+1)