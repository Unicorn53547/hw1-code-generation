# Write a python function to count the number of lists in a given number of lists.
def count_list(input_list):
    # Initialize a counter variable to keep track of the number of lists.
    count = 0
    # Iterate over each element in the input list.
    for element in input_list:
        # If the element is a list, increment the counter.
        if isinstance(element, list):
            count += 1
    # Return the total count of lists.
    return count

# Write a Python function to count the number of lists in a given list of lists of lists. The function should recursively count all the lists at any depth.
def count_lists_recursive(input_list):
    # Initialize a counter variable to keep track of the number of lists.
    count = 0
    # Iterate over each element in the input list.
    for element in input_list:
        # If the element is a list, recursively call the function on the element and add the result to the count.
        if isinstance(element, list):
            count += count_lists_recursive(element)
    # Return the total count of lists.
    return count

assert count_lists_recursive([[1, 2], [3, [4, 5]], 6]) == 3
assert count_lists_recursive([1, 2, 3]) == 0
assert count_lists_recursive([[[1], [2, [3]]], [4, [5, [6]]]]) == 7
assert count_lists_recursive([]) == 0
assert count_lists_recursive([[[[[]]]]]) == 4