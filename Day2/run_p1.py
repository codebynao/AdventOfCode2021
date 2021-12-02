with open('./input.txt', 'r') as textInput:
    instructions = textInput.readlines()

horizontal_pos = 0
depth = 0

for instruction in instructions:
    direction, value = instruction.split(' ')
    value = int(value)
    if direction == 'forward':
        horizontal_pos += value
    elif direction == 'up':
        depth -= value
    else:
        # direction == 'down'
        depth += value

print(horizontal_pos, depth, horizontal_pos*depth)
