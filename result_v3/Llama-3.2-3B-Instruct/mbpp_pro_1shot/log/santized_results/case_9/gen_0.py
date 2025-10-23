# Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
def check_min_heap_helper(arr, i):
    # Check if the given index is within the bounds of the array
    if i < 0 or i >= len(arr):
        return False

    # Check if the left child exists and is smaller than the parent
    left_child = 2 * i + 1
    if left_child < len(arr) and arr[left_child] < arr[i]:
        return False

    # Check if the right child exists and is smaller than the parent
    right_child = 2 * i + 2
    if right_child < len(arr) and arr[right_child] < arr[i]:
        return False

    # If no smaller child is found, the current node is a min heap
    return True

# Given a list of arrays, determine if each array represents a min heap. Return a list of boolean values where each value indicates whether the corresponding array is a min heap or not.
def check_min_heaps(arrays):
    result = []
    for array in arrays:
        # Check if the array is a min heap by recursively calling the helper function
        result.append(check_min_heap_helper(array, 0))
    return result

assert check_min_heaps([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 2, 4, 5]]) == [True, False, True]