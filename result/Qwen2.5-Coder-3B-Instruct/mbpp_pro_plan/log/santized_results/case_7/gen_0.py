# Write a function that returns the list in a list of lists whose sum of elements is the highest.
def max_sum_list(lists):
    # Initialize variables to keep track of the maximum sum and the corresponding list
    max_sum = float('-inf')
    max_list = None
    
    # Iterate through each list in the input list
    for lst in lists:
        # Calculate the sum of elements in the current list
        current_sum = sum(lst)
        
        # Check if the current sum is greater than the maximum sum found so far
        if current_sum > max_sum:
            # Update the maximum sum and the corresponding list
            max_sum = current_sum
            max_list = lst
    
    # Return the list with the highest sum
    return max_list

# Given a list of lists of lists, where each sub-list contains integers, write a function that returns the list of lists whose sum of elements is the highest among all sub-lists. If there are multiple lists with the same highest sum, return the first one encountered.
def max_sum_list_of_lists(list_of_lists):
    # Initialize variables to keep track of the maximum sum and the corresponding list
    max_sum = float('-inf')
    max_list = None
    
    # Iterate through each list in the input list
    for lst in list_of_lists:
        # Calculate the sum of elements in the current list
        current_sum = sum(lst)
        
        # Check if the current sum is greater than the maximum sum found so far
        if current_sum > max_sum:
            # Update the maximum sum and the corresponding list
            max_sum = current_sum
            max_list = lst
    
    # Return the list with the highest sum
    return max_list

assert max_sum_list_of_lists([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) == [[5, 6], [7, 8]]
assert max_sum_list_of_lists([[[1], [2, 3]], [[4], [5, 6]]]) == [[4], [5, 6]]
assert max_sum_list_of_lists([[[1, 2, 3], [4, 5]], [[6, 7], [8, 9]]]) == [[6, 7], [8, 9]]
assert max_sum_list_of_lists([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]) == [[9, 10], [11, 12]]