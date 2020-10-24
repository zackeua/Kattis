x, y = list(map(int,input().split()))
while x != 0 and y != 0:
        if x + y == 13:
                print('Never speak again.')
        elif x == y:
                print('Undecided.')
        elif x < y:
                print('Left beehind.')
        elif x > y:
                print('To the convention.')
        x, y = list(map(int,input().split()))