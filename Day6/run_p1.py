with open('./input.txt', 'r') as textInput:
    data = textInput.readlines()

# every 7 days
limit = 80
current_day = 0
fish_list = [int(fish) for fish in data[0].split(',')]

while current_day < limit:
    current_day += 1
    updated_fish_list = fish_list[:]
    for i in range(len(fish_list)):
        if fish_list[i] == 0:
            updated_fish_list[i] = 6
            updated_fish_list.append(8)
        else:
            updated_fish_list[i] = fish_list[i] - 1
    fish_list = updated_fish_list[:]

print(len(fish_list))
