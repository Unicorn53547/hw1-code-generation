# Write a function to find the sum of the largest contiguous sublist in the given list.
def max_sub_array_sum(a, size):
    """
    This function calculates the maximum sum of a contiguous sublist in the given list.

    Args:
        a (list): The input list of integers.
        size (int): The size of the sublist.

    Returns:
        int: The maximum sum of a contiguous sublist.
    """
    max_sum = float('-inf')  # Initialize max_sum as negative infinity
    for i in range(len(a) - size + 1):  # Iterate over the list with a sliding window of size 'size'
        window_sum = sum(a[i:i + size])  # Calculate the sum of the current window
        max_sum = max(max_sum, window_sum)  # Update max_sum if the current window sum is larger
    return max_sum

# Given a 2D list (matrix) of integers, find the sum of the largest contiguous submatrix.
def max_submatrix_sum(matrix):
    """
    This function calculates the maximum sum of a contiguous submatrix in the given matrix.

    Args:
        matrix (list): A 2D list of integers.

    Returns:
        int: The maximum sum of a contiguous submatrix.
    """
    rows, cols = len(matrix), len(matrix[0])  # Get the number of rows and columns in the matrix
    max_sum = float('-inf')  # Initialize max_sum as negative infinity

    # Iterate over all possible submatrices
    for left in range(cols):  # Left boundary of the submatrix
        for right in range(left, cols):  # Right boundary of the submatrix
            # Calculate the sum of the current submatrix
            submatrix_sum = 0
            for i in range(rows):
                for j in range(left, right + 1):
                    submatrix_sum += matrix[i][j]

            # Update max_sum if the current submatrix sum is larger
            max_sum = max(max_sum, submatrix_sum)

    return max_sum


assert max_submatrix_sum([[1, 2, -1], [-3, 4, 5], [6, -7, 8]]) == 15
assert max_submatrix_sum([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]) == 0
assert max_submatrix_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 45
assert max_submatrix_sum([[1, -2, 3], [4, 5, -6], [-7, 8, 9]]) == 17