# Write a function that returns the list in a list of lists whose sum of elements is the highest.
def max_sum_list(lists):
    # Initialize the maximum sum and the corresponding list
    max_sum = float('-inf')
    max_sum_list = None

    # Iterate over each list in the input list
    for lst in lists:
        # Calculate the sum of the current list
        current_sum = sum(lst)

        # If the current sum is greater than the maximum sum found so far, update the maximum sum and the corresponding list
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_list = lst

    # Return the list with the maximum sum
    return max_sum_list

assert max_sum_list_of_lists([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) == [[5, 6], [7, 8]]
assert max_sum_list_of_lists([[[1], [2, 3]], [[4], [5, 6]]]) == [[4], [5, 6]]
assert max_sum_list_of_lists([[[1, 2, 3], [4, 5]], [[6, 7], [8, 9]]]) == [[6, 7], [8, 9]]
assert max_sum_list_of_lists([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]) == [[9, 10], [11, 12]]