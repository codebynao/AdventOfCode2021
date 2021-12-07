from statistics import median

with open('./input.txt', 'r') as textInput:
    data = textInput.readlines()

crabs_positions = [int(crab_position) for crab_position in data[0].split(',')]

print(int(sum([abs(median(crabs_positions) - position) for position in crabs_positions])))
