import sys

data = list(sys.stdin)[1:]

count = 0
for row in data:
    r = row.upper()
    if 'ROSE' in r or 'PINK' in r:
        count += 1
print(count if count != 0 else 'I must watch Star Wars with my daughter')
