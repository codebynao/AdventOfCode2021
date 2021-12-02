with open('./input.txt', 'r') as textInput:
    depths = textInput.readlines()

totalIncrease = 0
previousDepth = depths.pop(0)
for depth in depths:
    if int(depth) > int(previousDepth):
        totalIncrease += 1
    previousDepth = depth
print(totalIncrease)
