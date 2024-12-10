from inputs import input_data_day_9
#PART ONE
def parseInput(input_data):
    string = ""
    for line in input_data.strip().split("\n"):
        string += line
    return string

nums = [int(num) for num in parseInput(input_data_day_9)]
hardware = []
position = 0
for i, num in enumerate(nums):
    if i % 2 == 0:
        new_block = [position] * num
        position += 1
    else:
        new_block = ["."] * num
    hardware.extend(new_block)
print(hardware)

l = 0
r = len(hardware) - 1
while l < r:
    while l < len(hardware) and hardware[l] != ".":
        l += 1
    while r > 0 and hardware[r] == ".":
        r -= 1

    hardware[l], hardware[r] = hardware[r], hardware[l]

print(hardware)
hardware[l], hardware[r] = hardware[r], hardware[l]
result = 0
i = 0
while hardware[i] != ".":
    result += i * hardware[i]
    i += 1
print(result)

#PART TWO
def parseInput(input_data):
    string = ""
    for line in input_data.strip().split("\n"):
        string += line
    return string
    

def compact_files(hardware):
    n = len(hardware)
    file_ids = sorted(set(hardware) - {"."}, reverse=True)  # Descending file IDs

    for file_id in file_ids:
        file_indices = [i for i, block in enumerate(hardware) if block == file_id]
        file_length = len(file_indices)

        free_start = -1
        free_length = 0

        for i in range(n):
            if hardware[i] == ".":
                if free_start == -1:
                    free_start = i
                free_length += 1
                if free_length == file_length and free_start <= file_indices[0]:
                    for idx in file_indices:
                        hardware[idx] = "."
                    for j in range(file_length):
                        hardware[free_start + j] = file_id
                    break
            else:
                free_start = -1
                free_length = 0

    return hardware


def calculate_checksum(hardware):
    checksum = 0
    for i, block in enumerate(hardware):
        if block != ".":
            checksum += i * int(block)
    return checksum



nums = [int(num) for num in parseInput(input_data_day_9)]
hardware = []
position = 0
for i, num in enumerate(nums):
    if i % 2 == 0:
        hardware.extend([position] * num)
        position += 1
    else:
        hardware.extend(["."] * num)
hardware = compact_files(hardware)
result = calculate_checksum(hardware)

print(f"Resulting checksum: {result}")