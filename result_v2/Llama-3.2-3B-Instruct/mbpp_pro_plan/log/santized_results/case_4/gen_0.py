# Write a function to find nth centered hexagonal number.
def centered_hexagonal_number(n):
    """
    Calculate the nth centered hexagonal number.

    The centered hexagonal number is defined as the sum of the first n natural numbers
    multiplied by the nth centered hexagonal number formula: (n*(n+1)*(2n+1))/6.

    Args:
        n (int): The position of the centered hexagonal number to calculate.

    Returns:
        int: The nth centered hexagonal number.
    """
    # Calculate the nth centered hexagonal number using the formula
    return (n * (n + 1) * (2 * n + 1)) // 6

# Given a list of integers representing the positions of points on a hexagonal grid, write a function to calculate the sum of the centered hexagonal numbers for each point in the list.
def sum_centered_hexagonal_numbers(points):
    """
    Calculate the sum of the centered hexagonal numbers for each point in the list.

    Args:
        points (list): A list of integers representing the positions of points on a hexagonal grid.

    Returns:
        int: The sum of the centered hexagonal numbers for each point in the list.
    """
    # Initialize the sum to 0
    total_sum = 0
    # Iterate over each point in the list
    for point in points:
        # Calculate the centered hexagonal number for the current point
        centered_hexagonal_num = centered_hexagonal_number(point)
        # Add the centered hexagonal number to the total sum
        total_sum += centered_hexagonal_num
    # Return the total sum
    return total_sum


assert sum_centered_hexagonal_numbers([1, 2, 3]) == 27
assert sum_centered_hexagonal_numbers([4, 5]) == 98
assert sum_centered_hexagonal_numbers([10]) == 271