# Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
def check_min_heap_helper(arr, i):
    """
    Helper function to check if the given array represents a min heap.
    
    Args:
    arr (list): The input array to be checked.
    i (int): The index of the current element in the array.
    
    Returns:
    bool: True if the array is a min heap, False otherwise.
    """
    # Check if the index is within the bounds of the array
    if i < 0 or i >= len(arr):
        return False
    
    # Check if the left child exists and is smaller than the current element
    left_child = 2 * i + 1
    if left_child < len(arr) and arr[left_child] < arr[i]:
        return False
    
    # Check if the right child exists and is smaller than the current element
    right_child = 2 * i + 2
    if right_child < len(arr) and arr[right_child] < arr[i]:
        return False
    
    # If all checks pass, the array is a min heap
    return True

# Given a list of arrays, determine if each array represents a min heap. Return a list of boolean values where each value indicates whether the corresponding array is a min heap or not.
def check_min_heaps(arrays):
    """
    Function to check if the given arrays represent min heaps.
    
    Args:
    arrays (list): A list of arrays to be checked.
    
    Returns:
    list: A list of boolean values where each value indicates whether the corresponding array is a min heap or not.
    """
    result = []
    for array in arrays:
        # Check each element in the array
        for i in range(len(array)):
            # If the current element is not a min heap, append False to the result list
            if not check_min_heap_helper(array, i):
                result.append(False)
                break
        else:
            # If all elements in the array are min heaps, append True to the result list
            result.append(True)
    return result

assert check_min_heaps([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 2, 4, 5]]) == [True, False, True]