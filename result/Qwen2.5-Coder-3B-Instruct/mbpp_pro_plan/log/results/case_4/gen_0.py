# Write a function to find nth centered hexagonal number.
def centered_hexagonal_number(n):
    # The formula for the nth centered hexagonal number is 3n(n-1) + 1
    return 3 * n * (n - 1) + 1

# Write a function to calculate the sum of the centered hexagonal numbers for each point in the list.
def sum_centered_hexagonal_numbers(points):
    # Initialize the sum to 0
    total_sum = 0
    # Iterate over each point in the list
    for point in points:
        # Calculate the centered hexagonal number for the current point
        hex_number = centered_hexagonal_number(point)
        # Add the centered hexagonal number to the total sum
        total_sum += hex_number
    # Return the total sum
    return total_sum

assert sum_centered_hexagonal_numbers([1, 2, 3]) == 27
assert sum_centered_hexagonal_numbers([4, 5]) == 98
assert sum_centered_hexagonal_numbers([10]) == 271