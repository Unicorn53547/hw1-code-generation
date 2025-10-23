# Write a function to find the number of ways to partition a set of Bell numbers.
def bell_number(n):
    # Initialize a list to store the Bell numbers
    bell = [1]
    # Calculate the Bell numbers iteratively
    for i in range(1, n+1):
        # Calculate the next Bell number as the sum of the previous Bell numbers
        bell.append(sum(bell))
    # Return the nth Bell number
    return bell[n]

# Given a list of integers representing the sizes of sets, write a function to find the total number of ways to partition all these sets combined.
def total_bell_numbers(sizes):
    # Initialize a variable to store the total number of ways
    total_ways = 1
    # Iterate over each set size
    for size in sizes:
        # Calculate the number of ways to partition the current set
        ways = bell_number(size)
        # Multiply the total number of ways by the number of ways to partition the current set
        total_ways *= ways
    # Return the total number of ways
    return total_ways

assert total_bell_numbers([1, 2, 3]) == 8
assert total_bell_numbers([0, 1, 2]) == 4
assert total_bell_numbers([5, 5, 5]) == 156
assert total_bell_numbers([10]) == 115975
assert total_bell_numbers([0, 0, 0]) == 3