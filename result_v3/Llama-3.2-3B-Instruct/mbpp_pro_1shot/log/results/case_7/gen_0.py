# Write a function that returns the list in a list of lists whose sum of elements is the highest.
def max_sum_list(lists):
    # Calculate the sum of each sub-list
    sums = [sum(sub_list) for sub_list in lists]
    # Find the index of the maximum sum
    max_sum_index = sums.index(max(sums))
    # Return the sub-list with the maximum sum
    return lists[max_sum_index]

assert max_sum_list_of_lists([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) == [[5, 6], [7, 8]]
assert max_sum_list_of_lists([[[1], [2, 3]], [[4], [5, 6]]]) == [[4], [5, 6]]
assert max_sum_list_of_lists([[[1, 2, 3], [4, 5]], [[6, 7], [8, 9]]]) == [[6, 7], [8, 9]]
assert max_sum_list_of_lists([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]) == [[9, 10], [11, 12]]