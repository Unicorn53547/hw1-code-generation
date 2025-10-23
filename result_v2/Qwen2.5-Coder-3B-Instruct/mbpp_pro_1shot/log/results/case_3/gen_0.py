# Write a function to find the number of ways to partition a set of Bell numbers.
def bell_number(n):
    # Base case: There is one way to partition a set of size 0
    if n == 0:
        return 1
    # Initialize the Bell number array
    bell = [0] * (n + 1)
    bell[0] = 1
    # Fill the Bell number array using the recurrence relation
    for i in range(1, n + 1):
        bell[i] = 0
        for j in range(i):
            bell[i] += bell[j] * bell[i - j - 1]
    return bell[n]

# Given a list of integers representing the sizes of sets, write a function to find the total number of ways to partition all these sets combined.
def total_bell_numbers(sizes):
    # Calculate the total number of ways to partition all sets combined
    total_ways = 1
    for size in sizes:
        total_ways *= bell_number(size)
    return total_ways

# Test the functions with the provided test case
assert total_bell_numbers([1, 2, 3]) == 8

assert total_bell_numbers([1, 2, 3]) == 8
assert total_bell_numbers([0, 1, 2]) == 4
assert total_bell_numbers([5, 5, 5]) == 156
assert total_bell_numbers([10]) == 115975
assert total_bell_numbers([0, 0, 0]) == 3