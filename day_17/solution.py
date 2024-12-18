import sys
import os

def parseInput():
    # Read the input file and parse registers and program
    dir_path = os.path.dirname(os.path.realpath(__file__))
    registers, program = open(f'{dir_path}/input.txt', 'r').read().split("\n\n")
    register_a, register_b, register_c = [int(line.split(": ")[1]) for line in registers.splitlines()]
    operations = [int(num) for num in program.strip()[9:].split(",")]
    return register_a, register_b, register_c, operations

def partOne():
    # Parse input and run the program for Part One
    register_a, register_b, register_c, program = parseInput()
    output = run_program(register_a, register_b, register_c, program)
    print(",".join(map(str, output)))

def partTwo():
    # Parse input and find the smallest register A for Part Two
    _, _, _, program = parseInput()
    possible_values = [(1, 0)]
    for depth, candidate_a in possible_values:
        for a in range(candidate_a, candidate_a + 8):
            result = run_program(a, 0, 0, program)
            if result == program:
                print(a)
                return
            possible_values.append((depth + 1, a * 8))

def run_program(register_a, register_b, register_c, program):
    instruction_pointer = 0
    output = []

    while True:
        if instruction_pointer >= len(program):
            break

        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        if opcode == 0:  # adv instruction
            register_a = register_a // (2 ** get_operand_value(operand, register_a, register_b, register_c))
        elif opcode == 1:  # bxl instruction
            register_b = operand ^ register_b
        elif opcode == 2:  # bst instruction
            register_b = get_operand_value(operand, register_a, register_b, register_c) % 8
        elif opcode == 3:  # jnz instruction
            if register_a != 0:
                instruction_pointer = operand - 2
        elif opcode == 4:  # bxc instruction
            register_b = register_b ^ register_c
        elif opcode == 5:  # out instruction
            output.append(get_operand_value(operand, register_a, register_b, register_c) % 8)
        elif opcode == 6:  # bdv instruction
            register_b = register_a // (2 ** get_operand_value(operand, register_a, register_b, register_c))
        elif opcode == 7:  # cdv instruction
            register_c = register_a // (2 ** get_operand_value(operand, register_a, register_b, register_c))

        instruction_pointer += 2

    return output

def get_operand_value(operand, register_a, register_b, register_c):
    operand_values = [operand, operand, operand, operand, register_a, register_b, register_c]
    return operand_values[operand]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py [one|two]")
        sys.exit(1)

    if sys.argv[1] == "one":
        partOne()
    elif sys.argv[1] == "two":
        partTwo()
    else:
        print("Invalid command. Use 'one' or 'two'.")
