from collections import defaultdict


def count_occurrences(numbers_list):
    number_counts = defaultdict(int)
    for num in numbers_list:
        number_counts[num] += 1
    return dict(number_counts)


# Example usage
my_numbers = [1, 2, 3, 2, 1, 4, 2, 5, 3, 3, 3]
result = count_occurrences(my_numbers)
print(result)  # Same output as before
