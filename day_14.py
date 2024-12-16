from inputs import input_data_day_14

def parse_input(input_data):
    robots = []
    for line in input_data.strip().split("\n"):
        parts = line.strip().split()
        px, py = map(int, parts[0][2:].split(','))
        vx, vy = map(int, parts[1][2:].split(','))
        robots.append(((px, py), (vx, vy)))
    return robots

def simulate_motion(robots, width, height, time):
    final_positions = []
    for (px, py), (vx, vy) in robots:
        final_x = (px + vx * time) % width
        final_y = (py + vy * time) % height
        final_positions.append((final_x, final_y))
    return final_positions

def calculate_quadrants(positions, width, height):
    mid_x = width // 2
    mid_y = height // 2
    quadrants = [0, 0, 0, 0]  

    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue  
        if x < mid_x and y < mid_y:
            quadrants[1] += 1  
        elif x >= mid_x and y < mid_y:
            quadrants[0] += 1 
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1 
        else:
            quadrants[3] += 1 

    return quadrants

def calculate_safety_factor(filename, width=101, height=103, time=100):
    robots = parse_input(filename)
    final_positions = simulate_motion(robots, width, height, time)
    quadrants = calculate_quadrants(final_positions, width, height)
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count
    return safety_factor

print(calculate_safety_factor(input_data_day_14))