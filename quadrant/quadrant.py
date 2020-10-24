import sys

coordinates = []

for coordinate in sys.stdin:
        coordinates.append(float(coordinate))

if(coordinates[0] > 0):
        if(coordinates[1] > 0):
                quadrant = 1
        else:
                quadrant = 4
else:
        if(coordinates[1] > 0):
                quadrant = 2
        else:
                quadrant = 3

print(quadrant)