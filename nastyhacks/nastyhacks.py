import sys

for row in list(sys.stdin)[1:]:
    l = list(map(int,row.split()))
    if l[0] > l[1] - l[2]:
        print("do not advertise")
    elif l[0] < l[1] - l[2]:
        print("advertise")
    else:
        print("does not matter")
