import sys


data = list(map(int,list(sys.stdin)[1:]))


kattis = sum([s*(4/5)**i for i,s in enumerate(data)])/5


avg = 0

for g in range(len(data)):
    l = [c for i,c in enumerate(data) if i != g]

    avg += sum([s*(4/5)**i for i,s in enumerate(l)])/5

avg = avg/len(data)


print(kattis)
print(avg)
