def change_number(num, count_map, old_count_map):
    if num == 0:
        count_map[1] = count_map.get(1, 0) + old_count_map[num]
    else:
        num_str = str(num)
        length = len(num_str)
        if length % 2 == 0:
            mid = length // 2
            left = int(num_str[:mid])
            right = int(num_str[mid:])
            count_map[left] = count_map.get(left, 0) + old_count_map[num]
            count_map[right] = count_map.get(right, 0) + old_count_map[num]
        else:
            new_num = num * 2024
            count_map[new_num] = count_map.get(new_num, 0) + old_count_map[num]


def solve(input_data, number_of_blinks):
    initial_numbers = list(map(int, input_data.split()))

    count_map = {}
    for num in initial_numbers:
        count_map[num] = count_map.get(num, 0) + 1


    for _ in range(number_of_blinks):
        new_count_map = {}
        for num in count_map:
            change_number(num, new_count_map, count_map)
        count_map = new_count_map

    return sum(count_map.values())


input_data_day_11 = "1750884 193 866395 7 1158 31 35216 0"
answer_part_one = solve(input_data_day_11, 25)
answer_part_two = solve(input_data_day_11, 75)
print(answer_part_one)
print(answer_part_two)
