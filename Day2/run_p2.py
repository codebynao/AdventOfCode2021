with open('./input.txt', 'r') as textInput:
    instructions = textInput.readlines()

horizontal_pos = 0
depth = 0
aim = 0

for instruction in instructions:
    direction, value = instruction.split(' ')
    value = int(value)
    if direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value
    else:
        # direction == 'forward'
        horizontal_pos += value
        depth += aim*value

print(horizontal_pos, depth, horizontal_pos*depth)
