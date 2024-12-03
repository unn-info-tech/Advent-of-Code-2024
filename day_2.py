
from inputs import input_data_day_2

def is_safe(report):
    increasing = True
    decreasing = True
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff < 1 or diff > 3:
            increasing = False
        if diff > -1 or diff < -3:
            decreasing = False
    return increasing or decreasing

def can_be_safe_by_removal(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

reports = [[int(level) for level in line.split()] for line in input_data_day_2.strip().split('\n')]

count_safe = 0
for report in reports:
    if is_safe(report):
        count_safe += 1
print("Number of Safe Reports (without removal):", count_safe)

count_safe_after_removal = 0
for report in reports:
    if can_be_safe_by_removal(report):
        count_safe_after_removal += 1
print("Number of Safe Reports (after removal):", count_safe_after_removal)
