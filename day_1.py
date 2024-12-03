from inputs import input_data_day_1
from collections import Counter

left_list = []
right_list = []

for line in input_data_day_1.strip().split('\n'):
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)



def diff_lists(left_list, right_list):
    left_list.sort()
    right_list.sort()
    return sum(abs(a - b) for a, b in zip(left_list, right_list))

def calculate_similarity_score(left_list, right_list):
    right_counts = Counter(right_list)
    return sum(left * right_counts[left] for left in left_list)

print("Total Distance:", diff_lists(left_list, right_list))
print("Similarity Score:", calculate_similarity_score(left_list, right_list))