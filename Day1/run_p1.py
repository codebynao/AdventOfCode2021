file = open(
    './input.txt', 'r')
depths = file.readlines()

totalIncrease = 0
previousDepth = depths.pop(0)
for depth in depths:
    if int(depth) > int(previousDepth):
        totalIncrease += 1
    previousDepth = depth
print(totalIncrease, len(depths))
