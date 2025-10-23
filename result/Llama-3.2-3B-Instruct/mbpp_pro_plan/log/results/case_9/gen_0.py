# Write a function to check if the given array represents min heap or not. https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/
def check_min_heap_helper(arr, i):
    # Check if the index is within the bounds of the array
    if i < 0 or i >= len(arr):
        return False

    # Check if the left child exists and is smaller than the root
    left_child = 2 * i + 1
    if left_child < len(arr) and arr[left_child] < arr[i]:
        return False

    # Check if the right child exists and is smaller than the root
    right_child = 2 * i + 2
    if right_child < len(arr) and arr[right_child] < arr[i]:
        return False

    # If no smaller child is found, the current node is a min heap
    return True

# Given a list of arrays, determine if each array represents a min heap or not.
def check_min_heaps(arrays):
    # Initialize an empty list to store the results
    results = []

    # Iterate over each array in the input list
    for array in arrays:
        # Initialize a flag to indicate if the array is a min heap
        is_min_heap = True

        # Iterate over each element in the array
        for i in range(len(array)):
            # Recursively call the helper function to check if the current element is a min heap
            if not check_min_heap_helper(array, i):
                # If the current element is not a min heap, set the flag to False and break the loop
                is_min_heap = False
                break

        # Append the result to the list
        results.append(is_min_heap)

    # Return the list of results
    return results

assert check_min_heaps([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 3, 2, 4, 5]]) == [True, False, True]