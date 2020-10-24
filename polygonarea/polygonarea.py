

n = int(input())

while n:

    i = 0
    S1 = 0
    S2 = 0
    x_0 = 0
    y_0 = 0
    x_p = 0
    y_p = 0
    while i < n:
        x, y = list(map(int, input().split()))

        S1 += x_p * y
        S2 += y_p * x

        if i == 0:
            x_0 = x
            y_0 = y
        
        x_p = x
        y_p = y
        i += 1

    S1 += x_p * y_0
    S2 += y_p * x_0

    area = 0.5 * (S1 - S2)
    direction = 'CCW' if area > 0 else 'CW'
    
    print(direction, abs(area))

    n = int(input())