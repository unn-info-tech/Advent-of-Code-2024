from inputs import input_data_day_8
def parseInput(input_data):
    parsed_input = []
    for line in input_data.strip().split('\n'):
        parsed_input.append(list(line))
    return parsed_input
parsed_input = parseInput(input_data_day_8)

#PART ONE
def find_antinodes(grid):
    rows, cols = len(grid), len(grid[0]) 
    antennas = []  
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.': 
                antennas.append((r, c, grid[r][c]))

    antinodes = set()  
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            r1, c1, freq1 = antennas[i]
            r2, c2, freq2 = antennas[j]

            if freq1 != freq2:
                continue  
            dr, dc = r2 - r1, c2 - c1

            x1 = (r1 - dr, c1 - dc)  
            x2 = (r2 + dr, c2 + dc)  

            if 0 <= x1[0] < rows and 0 <= x1[1] < cols:
                antinodes.add(x1)
            if 0 <= x2[0] < rows and 0 <= x2[1] < cols:
                antinodes.add(x2)

    return len(antinodes)



grid = [list(row) for row in parsed_input]

result = find_antinodes(grid)
print(f"Number of unique antinode locations: {result}")


#PART TWO
def find_antennas(grid):
    rows, cols = len(grid), len(grid[0])  
    antennas_map = {}  

    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if cell == '.':
                continue
            if cell not in antennas_map:
                antennas_map[cell] = []
            antennas_map[cell].append((r, c))

    antinodes = set() 

    for freq in antennas_map:
        antennas = antennas_map[freq]
        count = len(antennas)

        for r in range(count):
            A = antennas[r]
            antinodes.add(A)  

            for c in range(r + 1, count):
                B = antennas[c]
                diff = (A[0] - B[0], A[1] - B[1])  

                Ai, Aj = A
                while 0 <= Ai < rows and 0 <= Aj < cols:
                    antinodes.add((Ai, Aj))
                    Ai, Aj = Ai + diff[0], Aj + diff[1]

                Bi, Bj = B
                while 0 <= Bi < rows and 0 <= Bj < cols:
                    antinodes.add((Bi, Bj))
                    Bi, Bj = Bi - diff[0], Bj - diff[1]

    return len(antinodes)

grid = [list(row) for row in parsed_input]

result = find_antennas(grid)
print(f"Number of unique antinode locations: {result}")