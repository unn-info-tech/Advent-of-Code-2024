from collections import deque
import os
import sys

def parse_coordinates(input_string):
    lines = input_string.strip().split('\n')
    return [tuple(map(int, line.split(','))) for line in lines]

def create_grid(rows, cols, corrupted_positions):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    for i in range(1024):
        x, y = corrupted_positions[i]
        if 0 <= x < cols and 0 <= y < rows:  
            grid[y][x] = '#' 
    return grid

def bfs_shortest_path(grid, start, target):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, 0)])  

    grid[start[1]][start[0]] = '*'  

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (x, y), dist = queue.popleft()

        if (x, y) == target:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == '.':
                queue.append(((nx, ny), dist + 1))
                grid[ny][nx] = '*'  

    return -1


def parse_input():
  dir_path = os.path.dirname(os.path.realpath(__file__))
  return [[int(coor) for coor in line.split(",")] for line in open(f'{dir_path}/input.txt', 'r').read().splitlines()]

corrupted_positions = parse_input()
grid_size = 71
grid = create_grid(grid_size, grid_size, corrupted_positions)

start = (0, 0)
target = (70, 70)
shortest_path_length = bfs_shortest_path(grid, start, target)

print("Shortest path length:", shortest_path_length)


