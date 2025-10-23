# Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
def check_min_heap_helper(arr, i):
    n = len(arr)
    # Base case: if the current index is greater than or equal to the number of elements, return True
    if i >= n:
        return True
    # Check if the current element is greater than its left child
    if i * 2 + 1 < n and arr[i] > arr[i * 2 + 1]:
        return False
    # Check if the current element is greater than its right child
    if i * 2 + 2 < n and arr[i] > arr[i * 2 + 2]:
        return False
    # Recursively check the left and right subtrees
    return check_min_heap_helper(arr, i * 2 + 1) and check_min_heap_helper(arr, i * 2 + 2)

# Given a list of arrays, determine if each array represents a min heap. Return a list of boolean values where each value indicates whether the corresponding array is a min heap or not.
def check_min_heaps(arrays):
    results = []
    for arr in arrays:
        results.append(check_min_heap_helper(arr, 0))
    return results

assert check_min_heaps([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 2, 4, 5]]) == [True, False, True]