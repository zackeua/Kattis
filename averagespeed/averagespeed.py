import sys


data = list(sys.stdin)

distance = 0
t = -1
speed = 0
print('\n\n')
for row in data:
    line = row.split()
    hh, mm, ss = list(map(int,line[0].split(':')))
    time = hh + mm/60 + ss/3600
    #print(t)
    #print(time)
    if len(line) == 2:
        if t == -1:
            t = time
        else:
            distance += (speed * (time-t))
            t = time
        speed = float(line[1])
        #print(f'{line[0]} {distance} --')
    else:
        d = distance + speed * (time-t)
        print(f'{line[0]} {d:.2f} km')
    #print(speed)
