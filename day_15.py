from inputs import input_data_day_15

def parse_input(input_data):
    area, moves = input_data.strip().split("\n\n")
    grid = []
    for line in area.strip().split("\n"):
        grid.append(list(line))

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                return grid, moves, r, c



def calcuteGpsAfterMoves(input_data):
    grid, moves, r, c = parse_input(input_data)
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
    }

    for move in moves:
        if move == "\n":
            continue
        dr, dc = directions[move]
        nr, nc = r, c
        while grid[nr + dr][nc + dc] == "O":
            nr += dr
            nc += dc
        if grid[nr + dr][nc + dc] == "#":
            continue

        r += dr
        c += dc
        nr += dr
        nc += dc
        grid[nr][nc] = grid[r][c]
        grid[r][c] = "@"
        grid[r - dr][c  -dc] = '.'

    result = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                result += r * 100 + c
    return result




calcuteGpsAfterMoves(input_data_day_15)