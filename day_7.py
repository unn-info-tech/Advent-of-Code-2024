from inputs import input_data_day_7
equations = []
for line in input_data_day_7.strip().split('\n'):
    test_value, numbers = line.split(":")
    numbers = list(map(int, numbers.split()))
    equations.append((int(test_value), numbers))


# PART ONE
def evaluate_expression(test_value, numbers):
    operators = ["+", "*"]
    def backtracking(index, current_ops):
        if index == len(numbers) - 1:
            result = numbers[0]
            for i in range(1, len(numbers)):
                if current_ops[i - 1] == "+":
                    result += numbers[i]
                else:
                    result *= numbers[i]
            return result == test_value

        for operator in operators:
            current_ops.append(operator)
            if backtracking(index + 1, current_ops):
                return True
            current_ops.pop()
        return False
    return backtracking(0, [])


valid_sum = sum(test_value for test_value, numbers in equations if evaluate_expression(test_value, numbers))
print(f"Total calibration result: {valid_sum}")

# PART TWO
def evaluate_expression(test_value, numbers):
    operators = ['+', '*', "||"]
    def backtrack(index, current_ops):
        if index == len(numbers) - 1:
            result = numbers[0]
            for i in range(1, len(numbers)):
                if current_ops[i - 1] == '+':
                    result += numbers[i]
                elif current_ops[i - 1] == '*':
                    result *= numbers[i]
                elif current_ops[i - 1] == '||':
                    result = int(str(result) + str(numbers[i]))

            return result == test_value

        for op in operators:
            current_ops.append(op)
            if backtrack(index + 1, current_ops):
                return True
            current_ops.pop()
        return False

    return backtrack(0, [])





valid_sum = sum(test_value for test_value, numbers in equations if evaluate_expression(test_value, numbers))
print(f"Total calibration result: {valid_sum}")
