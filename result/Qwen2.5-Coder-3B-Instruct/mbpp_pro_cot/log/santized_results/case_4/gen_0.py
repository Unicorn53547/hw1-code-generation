# Write a function to find nth centered hexagonal number.
def centered_hexagonal_number(n):
    # The formula for the nth centered hexagonal number is 3n(n-1) + 1
    return 3 * n * (n - 1) + 1

# Write a function to calculate the sum of the centered hexagonal numbers for each point in the list.
def sum_centered_hexagonal_numbers(points):
    # Use the centered_hexagonal_number function to calculate the centered hexagonal number for each point
    return sum(centered_hexagonal_number(point) for point in points)

assert sum_centered_hexagonal_numbers([1, 2, 3]) == 27
assert sum_centered_hexagonal_numbers([4, 5]) == 98
assert sum_centered_hexagonal_numbers([10]) == 271