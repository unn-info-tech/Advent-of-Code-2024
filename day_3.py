from inputs import input_data_day_3
import re

def calculate_multiplications(corrupted_memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, corrupted_memory)
    total = 0
    for x, y in matches:
        total += int(x) * int(y)
    return total

def process_instructions(input_data):
    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")  # Matches valid mul(X,Y)
    control_pattern = re.compile(r"(do\(\)|don't\(\))")  # Matches do() or don't()

    mul_enabled = True
    total = 0

    instructions = re.split(control_pattern, input_data)

    for instruction in instructions:
        instruction = instruction.strip()

        if instruction == "do()":
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False

        elif mul_enabled:
            matches = mul_pattern.findall(instruction)
            for x, y in matches:
                total += int(x) * int(y) 

    return total


result_multiplications = calculate_multiplications(input_data_day_3)
print("Total from regular multiplications:", result_multiplications)

result_with_control = process_instructions(input_data_day_3)
print("Total with control instructions:", result_with_control)
