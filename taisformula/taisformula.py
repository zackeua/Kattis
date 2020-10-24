import sys

n = int(input())-1

prev = list(map(float,input().split()))
c = 0
area = 0
while c<n:
    current = list(map(float,input().split()))
    area += (current[0]-prev[0])*(current[1]+prev[1])/2
    prev = current
    c += 1
print(area/1000)
