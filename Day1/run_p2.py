with open('./input.txt', 'r') as textInput:
    depths = textInput.readlines()

totalIncrease = 0
lastThreeMeasurements = []
for _ in range(3):
    lastThreeMeasurements.append(int(depths.pop(0)))

lastTotalMeasurements = sum(lastThreeMeasurements)

for depth in depths:
    lastThreeMeasurements.pop(0)
    lastThreeMeasurements.append(int(depth))
    currentTotalMeasurements = sum(lastThreeMeasurements)
    if currentTotalMeasurements > lastTotalMeasurements:
        totalIncrease += 1
    lastTotalMeasurements = currentTotalMeasurements

print(totalIncrease)
