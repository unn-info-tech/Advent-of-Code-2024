from collections import defaultdict, deque
from inputs import input_data_day_5

def parse_input(input_data):
    rules_part, updates_part = input_data.strip().split("\n\n")
    
    pairs = [tuple(map(int, rule.split("|"))) for rule in rules_part.split("\n")]
    updates = [list(map(int, update.split(","))) for update in updates_part.split("\n")]
    
    rules = {}
    for a, b in pairs:
        rules[a] = rules.get(a, []) + [b]
    
    return rules, updates

def validate_and_reorder(input_data):
    rules, updates = parse_input(input_data)
    
    valid_updates = []
    invalid_updates = []
    
    for update in updates:
        valid = True
        for l in range(len(update)):
            for r in range(len(update) - 1, l, -1):
                if update[r] in rules and update[l] in rules[update[r]]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    def topological_sort(update, rules):
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        nodes = set(update)
        
        for a in nodes:
            for b in rules.get(a, []):
                if b in nodes:
                    graph[a].append(b)
                    in_degree[b] += 1
        
        queue = deque([node for node in nodes if in_degree[node] == 0])
        sorted_order = []
        
        while queue:
            node = queue.popleft()
            sorted_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return sorted_order

    reordered_updates = []
    for update in invalid_updates:
        reordered_updates.append(topological_sort(update, rules))

    sum_mid_reordered_updates = 0
    sum_mid_valid_updates = 0

    for update in reordered_updates:
        sum_mid_reordered_updates += update[len(update) // 2]

    for update in valid_updates:
        sum_mid_valid_updates += update[len(update) // 2]
    
    return sum_mid_reordered_updates, sum_mid_valid_updates




result = validate_and_reorder(input_data_day_5)
print("Sum of middle pages (reordered updates):", result[0])
print("Sum of middle pages (valid updates):", result[1])