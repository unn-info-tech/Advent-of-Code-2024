from inputs import data_input_day_6

# PART ONE
def dfs(r, c, direction):
    visited.add((r, c)) 
    while True:
        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            break

        if map[nr][nc] == "#":  
            direction = right_turn[direction]
        else:
            r, c = nr, nc
            visited.add((r, c))

    return len(visited)




directions = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}
right_turn = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

map = []
visited = set()
for line in data_input_day_6.strip().split("\n"):
    map.append(list(line))
rows = len(map)
cols = len(map[0])

starting_point = (0, 0)
starting_direction = "^"
for r in range(rows):
    for c in range(cols):
        if map[r][c] in directions:
            starting_point = (r, c)
            starting_direction = map[r][c]
            map[r][c] = "." 

result = dfs(starting_point[0], starting_point[1], starting_direction)
print(f"The guard visits {result} distinct positions.")


# PART TWO
directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}
right_turn = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}



grid = [list(line) for line in data_input_day_6.strip().split("\n")]
rows, cols = len(grid), len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] in directions:
            starting_point = (r, c)
            starting_direction = grid[r][c]
            grid[r][c] = "."  

def simulate_guard_path(r, c, direction, obstruction_pos):
    """
    Simulates the guard's movement.
    Returns True if a loop is detected.
    """
    visited = set()
    while True:
        if (r, c, direction) in visited:
            return True  
        visited.add((r, c, direction))

        dr, dc = directions[direction]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < rows and 0 <= nc < cols):
            break  

        if (nr, nc) == obstruction_pos or grid[nr][nc] == "#":
            direction = right_turn[direction] 
        else:
            r, c = nr, nc  

    return False  

valid_positions = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "." and (r, c) != starting_point:
            grid[r][c] = "#"

            if simulate_guard_path(*starting_point, starting_direction, (r, c)):
                valid_positions += 1

            grid[r][c] = "."

print(f"Number of valid positions to trap the guard in a loop: {valid_positions}")
