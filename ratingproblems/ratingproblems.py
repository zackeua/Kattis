n, k = list(map(int,input().split()))

avg = 0
i = 0

while i < k:
        avg += int(input())
        i += 1
print(f'{(avg -3*(n-k))/n} {(avg +3*(n-k))/n}')