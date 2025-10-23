# Write a function that returns the list in a list of lists whose sum of elements is the highest.
def max_sum_list(lists):
    max_sum = float('-inf')
    max_list = None
    for lst in lists:
        current_sum = sum(lst)
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = lst
    return max_list

# Given a list of lists of lists, where each sub-list contains integers, write a function that returns the list of lists whose sum of elements is the highest among all sub-lists. If there are multiple lists with the same highest sum, return the first one encountered.
def max_sum_list_of_lists(list_of_lists):
    max_sum = float('-inf')
    max_list = None
    for lst in list_of_lists:
        current_sum = sum(max_sum_list(lst))
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = lst
    return max_list

assert max_sum_list_of_lists([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) == [[5, 6], [7, 8]]

assert max_sum_list_of_lists([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) == [[5, 6], [7, 8]]
assert max_sum_list_of_lists([[[1], [2, 3]], [[4], [5, 6]]]) == [[4], [5, 6]]
assert max_sum_list_of_lists([[[1, 2, 3], [4, 5]], [[6, 7], [8, 9]]]) == [[6, 7], [8, 9]]
assert max_sum_list_of_lists([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]) == [[9, 10], [11, 12]]