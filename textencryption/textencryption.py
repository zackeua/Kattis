import re
n = int(input())

while n != 0:
    res = ''
    text = input()

    l = len(text)

    for i in range(l+1):
        res += text[(n*i)%l]
    res = re.sub(' ','', res).upper()
    print(res)

    n = int(input())
