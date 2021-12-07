with open('./input.txt', 'r') as textInput:
    data = textInput.readlines()

limit = 256
current_day = 0
fish_list = [int(fish) for fish in data[0].split(',')]

count_fish = [0] * 9

for i in range(len(fish_list)):
    count_fish[fish_list[i]] += 1

for i in range(limit):
    count_zero = count_fish[0]
    for j in range(1, 9):
        count_fish[j-1] = count_fish[j]
    count_fish[6] += count_zero
    count_fish[8] = count_zero

print(sum(count_fish))
