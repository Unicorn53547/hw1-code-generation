# Write a python function to count the number of lists in a given number of lists.
def count_list(input_list):
    count = 0
    for item in input_list:
        if isinstance(item, list):
            count += 1
    return count

# Write a Python function to count the number of lists in a given list of lists of lists. The function should recursively count all the lists at any depth.
def count_lists_recursive(input_list):
    count = 0
    for item in input_list:
        if isinstance(item, list):
            count += 1
            count += count_lists_recursive(item)
    return count

assert count_lists_recursive([[1, 2], [3, [4, 5]], 6]) == 3

assert count_lists_recursive([[1, 2], [3, [4, 5]], 6]) == 3
assert count_lists_recursive([1, 2, 3]) == 0
assert count_lists_recursive([[[1], [2, [3]]], [4, [5, [6]]]]) == 7
assert count_lists_recursive([]) == 0
assert count_lists_recursive([[[[[]]]]]) == 4