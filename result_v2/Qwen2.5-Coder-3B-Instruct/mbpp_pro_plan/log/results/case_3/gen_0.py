# Write a function to find the number of ways to partition a set of Bell numbers.
def bell_number(n):
    # Base case: There is one way to partition a set of size 0
    if n == 0:
        return 1
    # Initialize a list to store Bell numbers
    bell = [0] * (n + 1)
    # Base case: There is one way to partition a set of size 0
    bell[0] = 1
    # Fill the Bell number table
    for i in range(1, n + 1):
        # Initialize the current Bell number
        bell[i] = 0
        # Calculate the current Bell number using the previous Bell numbers
        for j in range(i):
            bell[i] += bell[j] * bell[i - j - 1]
    # Return the nth Bell number
    return bell[n]

# Write a function to find the total number of ways to partition all these sets combined.
def total_bell_numbers(sizes):
    # Initialize a list to store the total number of ways to partition each set
    total_ways = [0] * len(sizes)
    # Calculate the total number of ways to partition each set
    for i in range(len(sizes)):
        total_ways[i] = bell_number(sizes[i])
    # Return the total number of ways to partition all the sets combined
    return sum(total_ways)

assert total_bell_numbers([1, 2, 3]) == 8
assert total_bell_numbers([0, 1, 2]) == 4
assert total_bell_numbers([5, 5, 5]) == 156
assert total_bell_numbers([10]) == 115975
assert total_bell_numbers([0, 0, 0]) == 3