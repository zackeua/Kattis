import sys

data = list(sys.stdin)

result = []
for item in data:
        result.append(sum([int(i) for i in item.split()]))

maximum = max(result)
for i in range(len(result)):
        if (maximum == result[i]):
                print(f'{i+1} {maximum}')
