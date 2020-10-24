data = input()
D, M = map(int,data.split())
month = {1:0, 2:31, 3:28, 4:31,
        5:30, 6:31, 7:30, 8:31,
        9:31, 10:30, 11:31, 12:30}

day = {1:"Thursday", 2:"Friday",
    3:"Saturday", 4:"Sunday",
    5:"Monday", 6:"Tuesday",
    0:"Wednesday"}

total = 0

for i in range(1,M+1):
    total += month[i]

print(day[(total+D)%7])
