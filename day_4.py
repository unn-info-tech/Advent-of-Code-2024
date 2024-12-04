from inputs import input_data_day_4

def count_xmas_occurrences(grid, target):
    rows = len(grid)
    cols = len(grid[0])
    target_length = len(target)
    count = 0


    def check_direction(r, c, dr, dc):
        for i in range(target_length):
            nr, nc = r + i * dr, c + i * dc
            if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] != target[i]:

                return False
        return True

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),

        (1, 1),
        (-1, 1),
        (-1, -1),
        (1, -1)
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    return count

def count_x_mas_occurrences(grid):
    xmas_count = 0
    for r in range(1, len(grid) - 1):  
        line = grid[r]
        for c in range(1, len(line) - 1):  
            c_value = line[c] 
            if c_value == 'A':  
                
                lower_line = grid[r + 1]
                upper_line = grid[r - 1]
                low_left = lower_line[c - 1]
                low_right = lower_line[c + 1]
                up_left = upper_line[c - 1]
                up_right = upper_line[c + 1]

                low_left_to_right_up_is_valid = False
                low_right_to_up_left_is_valid = False

                if low_left == 'M' and up_right == 'S':
                    low_left_to_right_up_is_valid = True
                if low_left == 'S' and up_right == 'M':
                    low_left_to_right_up_is_valid = True
                if low_right == 'M' and up_left == 'S':
                    low_right_to_up_left_is_valid = True
                if low_right == 'S' and up_left == 'M':
                    low_right_to_up_left_is_valid = True

                if low_left_to_right_up_is_valid and low_right_to_up_left_is_valid:
                    xmas_count += 1
    return xmas_count


grid = [list(line) for line in input_data_day_4.strip().split('\n')]
target_word = "XMAS"
print("Total occurrences of XMAS:", count_xmas_occurrences(grid, target_word))
print("Total occurrences of X-MAS", count_x_mas_occurrences(grid))