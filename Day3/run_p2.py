with open('./input.txt', 'r') as textInput:
    data = textInput.readlines()

length = len(data[0].strip())


def get_most_common_number(list, index):
    total_zeros = 0
    total_ones = 0
    for item in list:
        if item[index] == '0':
            total_zeros += 1
        else:
            total_ones += 1

    if total_ones > total_zeros:
        return '1'
    elif total_ones < total_zeros:
        return '0'
    return None


def get_bit_criteria(list, index, is_oxygen_rating):
    most_common_number = get_most_common_number(list, index)
    if is_oxygen_rating:
        return most_common_number

    return '1' if most_common_number == '0' else '0'


def filter_list(list, index, comparison_value, default_value):
    filtered_list = []
    if comparison_value is None:
        comparison_value = default_value
    for item in list:
        if item[index] == comparison_value:
            filtered_list.append(item.strip())
    return filtered_list


def get_rating(data_list, default_value, is_oxygen_rating):
    bit_criteria = get_bit_criteria(data_list, 0, is_oxygen_rating)
    filtered_binary_numbers = filter_list(data_list, 0, bit_criteria, default_value)
    index = 1

    while len(filtered_binary_numbers) > 1 and index < length:
        bit_criteria = get_bit_criteria(filtered_binary_numbers, index, is_oxygen_rating)
        filtered_binary_numbers = filter_list(filtered_binary_numbers, index, bit_criteria, default_value)
        index += 1
    return filtered_binary_numbers[0] if len(filtered_binary_numbers) > 0 else None


oxygen_rating = get_rating(data, '1', True)
co2_rating = get_rating(data, '0', False)

life_support_rating = int(oxygen_rating, 2)*int(co2_rating, 2)
print(life_support_rating)
