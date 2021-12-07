with open('./input.txt', 'r') as textInput:
    data = textInput.readlines()

crabs_positions = [int(crab_position) for crab_position in data[0].split(',')]

costs = []
for cost in range(min(crabs_positions), max(crabs_positions) + 1):
    total = 0
    for position in crabs_positions:
        x = max(position, cost) - min(position, cost)
        total += (int(x * (x + 1) / 2))
    costs.append(total)

print(min(costs))
