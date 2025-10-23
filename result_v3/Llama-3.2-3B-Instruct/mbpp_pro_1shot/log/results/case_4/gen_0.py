# Write a function to find nth centered hexagonal number.
def centered_hexagonal_number(n):
    # The nth centered hexagonal number is given by the formula: (3n^2 - n) / 2
    return (3 * n ** 2 - n) // 2

# Given a list of integers representing the positions of points on a hexagonal grid, write a function to calculate the sum of the centered hexagonal numbers for each point in the list.
def sum_centered_hexagonal_numbers(points):
    # Initialize the sum to 0
    total_sum = 0
    # For each point in the list, calculate the centered hexagonal number and add it to the sum
    for point in points:
        total_sum += centered_hexagonal_number(point)
    # Return the total sum
    return total_sum

assert sum_centered_hexagonal_numbers([1, 2, 3]) == 27
assert sum_centered_hexagonal_numbers([4, 5]) == 98
assert sum_centered_hexagonal_numbers([10]) == 271