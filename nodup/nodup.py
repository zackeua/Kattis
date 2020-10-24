import sys

words = list(sys.stdin)[0].split()

unique = set(words)
print('no' if len(unique) < len(words) else 'yes')
