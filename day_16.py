

from collections import deque
import heapq

def parse_input(input_data):
    grid = []
    for line in input_data.strip().split("\n"):
        grid.append(list(line))
    return grid

def find_shortest_path(input_data):
    grid = parse_input(input_data)
    ROW, COL = len(grid), len(grid[0])
    sr, sc = ROW - 2, 1  
    er, ec = 1, COL - 2  
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  

    visited = set((sr, sc))  
    all_scores = []

    heap = [(0, sr, sc, (0, 1))]
    while heap:
        cost, r, c, direction = heapq.heappop(heap)
        if grid[r][c] == 'E':
            return cost

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if grid[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                newcost = 1
                if direction != (dr, dc):
                    newcost += 1000
                heapq.heappush(heap, (cost + newcost, nr, nc, (dr, dc)))
    return -1

input_data_day_16 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
#####.#####.#.#
#...#.....#.#.#
#.###.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

print(find_shortest_path(input_data_day_16))

import os
from collections import deque

def encode_position(i, j):
    return f"{i}:{j}"


input_data_day_16 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
#####.#####.#.#
#...#.....#.#.#
#.###.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""
def solve(grid):
    height = len(grid)
    width = len(grid[0])
    visited = {}
    moves = [
        (0, 1),  # right
        (1, 0),  # down
        (0, -1), # left
        (-1, 0)  # up
    ]

    def is_movable(i, j):
        return 0 <= i < height and 0 <= j < width and grid[i][j] != "#"

+    def is_visited(i, j):
        return encode_position(i, j) in visited

    def make_visited(grid, i, j, move_index, score):
        directions = [">", "v", "<", "^"]
        grid[i][j] = directions[move_index]
        visited[encode_position(i, j)] = score

    def get_movable_array(i, j, move_index):
        return [
            {
                "num": num,
                "score": 1 if num == 0 else 1001 if num in {1, 3} else 2001
            }
            for num in range(4)
            if is_movable(
                i + moves[(move_index + num) % len(moves)][0],
                j + moves[(move_index + num) % len(moves)][1]
            )
        ]

    # Find the starting position
    queue = deque()
    for i in range(height):
        for j in range(width):
            if grid[i][j] == "S":
                queue.append((i, j, 0, 0, []))

    # Perform BFS
    min_score = float('inf')
    tiles = []
    while queue:
        i, j, score, move_index, tile_indexes = queue.popleft()

        # If at the finish line
        if grid[i][j] == "E":
            if score < min_score:
                min_score = score
                tiles = tile_indexes[:]
            elif score == min_score:
                for tile in tile_indexes:
                    if tile not in tiles:
                        tiles.append(tile)
            continue

        # Movable directions
        move_arr = get_movable_array(i, j, move_index)
        if is_visited(i, j) and visited[encode_position(i, j)] < score:
            # Double-check
            if not any(
                not is_visited(
                    next_i := i + moves[(move_index + move["num"]) % len(moves)][0],
                    next_j := j + moves[(move_index + move["num"]) % len(moves)][1]
                ) or visited.get(encode_position(next_i, next_j), float('inf')) >= score + move["score"]
                for move in move_arr
            ):
                continue
        else:
            make_visited(grid, i, j, move_index, score)

        # Legal moves
        for move in move_arr:
            next_i = i + moves[(move_index + move["num"]) % len(moves)][0]
            next_j = j + moves[(move_index + move["num"]) % len(moves)][1]
            queue.append((
                next_i,
                next_j,
                score + move["score"],
                (move_index + move["num"]) % len(moves),
                tile_indexes + [(i, j)]
            ))

    return len(tiles) + 1



answer = solve(parse_input(input_data_day_16))
print(answer)
