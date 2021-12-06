import numpy as np

with open('./input.txt', 'r') as textInput:
    data = textInput.readlines()

# Parse data as [[(x1, y1), (x2, y2)], [(x3, y3), (x4, y4)]]
vents = []
for line in data:
    vents.append([tuple([int(coord) for coord in coords.split(',')]) for coords in line.split('->')])

field = np.zeros([1000, 1000], dtype=int)

for vent in vents:
    # is a diagonal vent
    if vent[0][0] != vent[1][0] and vent[0][1] != vent[1][1]:
        continue
    for x in range(min(vent[0][0], vent[1][0]), max(vent[0][0], vent[1][0])+1):
        for y in range(min(vent[0][1], vent[1][1]), max(vent[0][1], vent[1][1])+1):
            field[x][y] += 1


# Get all the values of field that are >= 2 and sum them up
print((field >= 2).sum())
