from inputs import input_data_day_16
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



print(find_shortest_path(input_data_day_16))
