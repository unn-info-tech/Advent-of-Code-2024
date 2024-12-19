
import os, sys
#PART ONE
def parse_input():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parts = open(f'{dir_path}/input.txt', 'r').read().strip().split("\n\n")
    patterns = parts[0].split(", ")
    designs = parts[1].split("\n")
    return patterns, designs


def can_form_design(design, patterns, memo):
    if design in memo:  # Memoization to avoid redundant calculations
        return memo[design]
    if design == "":  # Base case: successfully matched entire design
        return 1
    ways = 0
    for pattern in patterns:
        if design.startswith(pattern):  # Check if pattern matches the start
            if can_form_design(design[len(pattern):], patterns, memo):
                memo[design] = True
                return True
    memo[design] = False
    return False

patterns, designs = parse_input()
memo = {}
count = 0

# Check each design
for design in designs:
    if can_form_design(design, patterns, memo):
        count += 1

print("Number of possible designs:", count)


# PART TWO

# Memoized recursive function to count the number of ways to form the design
def count_ways_recursive(patterns, design, start, memo):
    # If we have reached the end of the design, return 1 as this is a valid arrangement
    if start == len(design):
        return 1
    
    # If we've already computed the number of ways for this position, return it
    if start in memo:
        return memo[start]
    
    ways = 0
    # Try each pattern and check if it matches the substring starting from `start`
    for pattern in patterns:
        if design[start:start + len(pattern)] == pattern:
            ways += count_ways_recursive(patterns, design, start + len(pattern), memo)
    
    # Cache the result for the current position
    memo[start] = ways
    return ways

def solve():
    patterns, designs = parse_input()
    total_ways = 0

    for design in designs:
        # Use memoization to store the results of subproblems
        memo = {}
        ways = count_ways_recursive(patterns, design, 0, memo)
        total_ways += ways
    
    print("Total number of ways:", total_ways)
    return total_ways

solve()
