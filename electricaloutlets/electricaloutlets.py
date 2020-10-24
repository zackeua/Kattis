import sys


data = list(sys.stdin)[1:]


for row in data:
    nums = map(int,row.split())
    for i, num in enumerate(nums):
        if i == 0:
            count = 0
        elif i == 1:
            count += num
        else:
            count += (num - 1)
    print(f'{count}')
