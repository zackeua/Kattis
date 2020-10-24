import sys

N = int(input())

count = 0

while count < N:
    s = input()
    s = s.lower()
    missing = ""
    for c in range(ord('a'),ord('z')+1):
        if not chr(c) in s:
            missing += chr(c)
    if missing == "":
        print("pangram")
    else:
        print(f'missing {missing}')
    count += 1
