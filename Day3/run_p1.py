with open('./input.txt', 'r') as textInput:
    data = textInput.readlines()

length = len(data[0].strip())
total_zeros = [0 for i in range(length)]
total_ones = [0 for i in range(length)]

for binary_number in data:
    for i in range(len(binary_number.strip())):
        if binary_number[i] == '0':
            total_zeros[i] += 1
        else:
            total_ones[i] += 1

most_common_values = []
least_common_values = []

for i in range(length):
    if total_zeros[i] > total_ones[i]:
        most_common_values.append('0')
        least_common_values.append('1')
    else:
        most_common_values.append('1')
        least_common_values.append('0')
gamma_rate = ''.join(most_common_values)
epsilon_rate = ''.join(least_common_values)

# Convert from binary to decimal and multiply
power_consumption = int(gamma_rate, 2)*int(epsilon_rate, 2)
print(power_consumption)
