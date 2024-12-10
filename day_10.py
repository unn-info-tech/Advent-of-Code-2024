from inputs import input_data_day_10


def parseInput(input_data):
    grid = []
    for line in input_data.strip().split("\n"):
        grid.append([int(num) for num in line])
    return grid
input_data = parseInput(input_data_day_10)

def numberOfScores(grid):
    scores = {}
    scores_ratings = {}

    def dfs(r, c, trailhead):
        if grid[r][c] == 9:
            if (r, c) not in scores[trailhead]:
                scores[trailhead].append((r, c))
            scores_ratings[trailhead] += 1
            return
        directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
        ]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == grid[r][c] + 1:
                dfs(nr, nc, trailhead)
        return



    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                trailhead = (r, c)
                scores[trailhead] = []
                scores_ratings[trailhead] = 0
                dfs(r, c, trailhead)
    
    return (sum([len(arr) for arr in scores.values()]), sum(scores_ratings.values()))

result = numberOfScores(input_data)
print(result)