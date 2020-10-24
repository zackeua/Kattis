from sys import stdin


data = list(stdin)

count = 0
for first, second in zip(data[1:-1], data[2:]):
    count += first == second

print(count)
